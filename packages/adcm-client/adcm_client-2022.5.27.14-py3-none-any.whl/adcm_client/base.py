# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# pylint: disable=R0901
import json
from collections import UserList, OrderedDict
from contextlib import contextmanager
from functools import wraps
from pprint import pprint
from time import sleep

from version_utils import rpm

from adcm_client.util.search import search_one, search
from adcm_client.wrappers.api import ADCMApiWrapper

# necessary for backward compatibility
# pylint: disable=unused-import
from adcm_client.wrappers.api import ActionHasIssues, ResponseTooLong

# If we are running the client from tests with Allure we expected that code
# to trace steps in Allure UI.
# But in case of running client outside of testing Allure is useless in virtualenv.
# So that code should be flexible enought to work with Allure or without.
ALLURE = True
try:
    import allure
except ImportError:
    ALLURE = False


# That is trick which is almost the same that in _allure.py::StepContext
# We have a function that can be used as contextmanager and decorator
# in same time.
@contextmanager
def dummy_context(*args, **kwargs):
    yield


def allure_step(text):
    if ALLURE:
        return allure.step(text)
    return dummy_context(text)


def allure_attach_json(body, name):
    if ALLURE:
        allure.attach(
            json.dumps(body, indent=2),
            name=name,
            attachment_type=allure.attachment_type.TEXT,
        )


def allure_attach(body, name, extension):
    if ALLURE:
        allure.attach(
            body=body,
            name=name,
            extension=extension,
        )


def pp(*args, **kwargs):
    pprint("--------------------------------------------------")
    if args:
        pprint(args)
    if kwargs:
        pprint(kwargs)
    pprint("--------------------------------------------------")


def strip_none_keys(args):
    """Usefull function to interact with coreapi.

    While it's ok to pass function arguments with default equal to None,
    it is not allowed to pass it over coreapi. So we have to strip keys
    with None values.
    """
    return {k: v for k, v in args.items() if v is not None}


class TooManyArguments(Exception):
    pass


class NoSuchEndpointOrAccessIsDenied(Exception):
    pass


class ObjectNotFound(Exception):
    pass


class WaitTimeout(Exception):
    pass


class ADCMApiError(Exception):
    pass


class PagingEnds(Exception):
    """There are no more data in paginated mode."""


class TooOldServerVersion(Exception):
    """Incompatible version, upgrade version ADCM."""

    def __init__(self, method_name='', version='', message=None):
        if message is None:
            self.message = (
                f'The "{method_name}" method works with versions older {version},'
                f' upgrade version ADCM.'
            )
        else:
            self.message = message
        super().__init__(self.message)


def min_server_version(version):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # The ADCM version must be greater than or equal to the method version
            # args[0].adcm_version >= version
            if rpm.compare_versions(args[0].adcm_version, version) < 0:
                raise TooOldServerVersion(func.__name__, version)
            return func(*args, **kwargs)

        return wrapper

    return decorate


def legacy_server_implementaion(oldfunc, turnover_version):
    """Replace function with oldfunc if version of server < turnover_version

    This decorator is usefull in case you have two way to do almost the same for
    new server and for old server. For example you have new, more efficient calls.

    There is a restriction of using this decorator. You should not patch legacy and
    non legacy functions with setattr. Because we call original class functions from
    inner wrapper.
    But any you are not so dirty, don't you?
    """

    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            # adcm_version >= turnover_versions
            if rpm.compare_versions(self.adcm_version, turnover_version) < 0:
                return oldfunc(self, *args, **kwargs)
            return func(self, *args, **kwargs)

        return wrapper

    return decorator


class Paging:
    def __init__(self, paged_object, limit=50, **args):
        self._paged_object = paged_object
        self._limit = limit
        self._query_params = args  # Just passing it to paged_object
        self._offset = 0  # Offset in paging
        self._current_list = None  # Current page data
        self._current_iterator = None

    def __iter__(self):
        self._offset = 0
        return self

    def __next_list(self):
        try:
            result = self._paged_object(
                paging={'limit': self._limit, 'offset': self._offset}, **self._query_params
            )
            self._offset += self._limit
            self._current_list = result
            self._current_iterator = iter(self._current_list)
        except PagingEnds:
            raise StopIteration from None

    def __next_element(self):  # pylint: disable=unused-private-member
        return next(self._current_iterator)

    def __next__(self):
        if self._current_iterator is None:
            self.__next_list()

        while True:
            try:
                result = next(self._current_iterator)
                return result
            except StopIteration:
                self.__next_list()


def _merge(*args, **kwargs):
    result = {}
    for i in args:
        result.update(i)
    result.update(kwargs)
    return result


def _find_endpoint(api, path):
    result = api
    if path is not None:
        for i in path:
            if i in result.__dict__:
                result = result.__dict__[i]
            else:
                raise NoSuchEndpointOrAccessIsDenied
    return result


class EndPoint:
    def __init__(self, api, idname, path, path_args=None, awailable_filters=None):
        if idname is None:
            raise NotImplementedError

        self.point = _find_endpoint(api.objects, path)

        self.idname = idname

        if awailable_filters is None:
            self.awailable_filters = []
        elif isinstance(awailable_filters, list):
            self.awailable_filters = awailable_filters
        else:
            raise NotImplementedError

        if path_args is None:
            self.path_args = {}
        else:
            self.path_args = path_args

    def _get_filters_value(self, **args):
        result = {}
        for v in self.awailable_filters:
            # There is a dirty case when we have one Class for two endpoints
            # That is Host class. When it works as Cluster child (cluster/4/host)
            # it has cluster_id in path. But when it used as single object (/host/4)
            # it has cluster_id in filters
            if v in args and v not in self.path_args:
                result[v] = args[v]
        return result

    def list(self, paging=None, **args):
        if paging is None:
            paging = {}
        filters = self._get_filters_value(**args)
        try:
            result = self.point.list(**self.path_args, **paging, **filters)
        except AttributeError as error:
            raise NoSuchEndpointOrAccessIsDenied from error

        if isinstance(result, OrderedDict):
            # It's paging mode
            if not result['results'] and 'offset' in paging and 'limit' in paging:
                raise PagingEnds
            return result['results']
        elif isinstance(result, list) and 'offset' in paging and paging['offset']:
            raise PagingEnds
        return result

    def read(self, object_id):
        try:
            return self.point.read(**self.get_object_path(object_id))
        except AttributeError as error:
            raise NoSuchEndpointOrAccessIsDenied from error

    def search(self, paging=None, **args):
        # TODO: Add filtering on backend
        return search(self.list(paging, **args), **args)

    def search_one(self, **args):
        # FIXME: paging
        if self.idname in args:
            return self.read(args[self.idname])
        data = None
        for obj in Paging(self.list, **args):
            data = search_one([obj], **args)
            if data is not None:
                break
        if data is None:
            raise ObjectNotFound

        return self.read(data['id'])

    def get_object_path(self, object_id):
        return _merge(self.path_args, {self.idname: object_id})

    def get_subpoint(self, *path):
        return _find_endpoint(self.point, path)

    def delete(self, object_id):
        try:
            return self.point.delete(**self.get_object_path(object_id))
        except AttributeError as error:
            raise NoSuchEndpointOrAccessIsDenied from error

    def update(self, object_id, **kwargs):
        try:
            kwargs.update(self.get_object_path(object_id))
            return self.point.partial_update(**kwargs)
        except AttributeError as error:
            raise NoSuchEndpointOrAccessIsDenied from error


class BaseAPIObject:
    """That is common object for single ADCM's object"""

    IDNAME = None  # Will not be None in child
    PATH = None  # Will not be None in child
    FILTERS = []

    def _register_attrs(self):
        for k, v in self._data.items():
            if hasattr(self, k) and not callable(getattr(self, k)):
                setattr(self, k, v)

    def _copy_path_args(self, *names):
        for i in names:
            self._path_args[i] = self._data[i]

    def _merge(self, *args, **kwargs):
        return _merge(self._endpoint.get_object_path(self.id), *args, **kwargs)

    def __init__(self, api: ADCMApiWrapper, path=None, path_args=None, **args):
        if path is None and self.PATH is None and self.SUBPATH is None:
            raise NotImplementedError

        if path is None:
            # When we have some solid object like cluster,
            # it has a PATH list in class
            path = self.PATH

        if self.PATH is None:
            # If we have some object which is not hight level, like
            # cluster/<id>/action - host/<id>/action
            # In that case action is subobject and path should be
            # constructed somewhere out of scope.
            self.PATH = path

        self._endpoint = EndPoint(api, self.IDNAME, path, path_args, self.FILTERS)
        self._api = api
        self.adcm_version = self._api.adcm_version
        self._client = api.objects

        self._data = self._endpoint.search_one(**args)

        if self._data is None:
            raise ObjectNotFound

        # TODO: Do something with id name consistency in Engine
        self._data[self.IDNAME] = self._data['id']
        # self._copy_path_args(self.IDNAME)
        self._register_attrs()

    def reread(self):
        self._data = self._endpoint.read(self.id)
        if self._data is None:
            raise ObjectNotFound
        self._register_attrs()

    def wait_for_attr(self, attrname, values, timeout=None, interval=None):
        if timeout is None:
            timeout = 86400
        if interval is None:
            interval = 0.2
        i = 0
        while getattr(self, attrname) not in values and i < timeout:
            sleep(interval)
            i = i + interval
            self.reread()
        if self.status in values:
            return self.status
        raise WaitTimeout

    def _subobject(self, classname, **args):
        return classname(
            self._api,
            path=self.PATH + classname.SUBPATH,
            path_args=self._endpoint.get_object_path(self.id),
            **args,
        )

    def _subcall(self, *path, **args):
        func = self._endpoint.get_subpoint(*path)
        return func(**self._merge(**args))

    def _sub_call(self, *path, **args):
        """Makes a request to the API by path with required lookup params"""
        # the same as _subcall(), only without _merge()
        func = self._endpoint.get_subpoint(*path)
        return func(**args)

    def _child_obj(self, classname, **args):
        return classname(self._api, **_merge(args, {self.IDNAME: self.id}))

    def _parent_obj(self, classname):
        return classname(self._api, **{classname.IDNAME: self._data[classname.IDNAME]})

    def delete(self):
        return self._endpoint.delete(self.id)

    def update(self, **kwargs) -> None:
        self._endpoint.update(self.id, **kwargs)
        self.reread()


class BaseAPIListObject(UserList):  # pylint: disable=too-many-ancestors
    """That is common object for multiple ADCM's object"""

    _ENTRY_CLASS = BaseAPIObject

    def __init__(self, api: ADCMApiWrapper, path=None, path_args=None, paging=None, **args):
        self._api = api
        self._client = api.objects
        if path_args is None:
            self._path_args = {}
        else:
            self._path_args = path_args

        if path is None:
            path = self._ENTRY_CLASS.PATH

        self._endpoint = EndPoint(
            api, self._ENTRY_CLASS.IDNAME, path, path_args, self._ENTRY_CLASS.FILTERS
        )
        data = []
        for i in self._endpoint.search(**args, paging=paging):
            data.append(
                self._ENTRY_CLASS(
                    api, path=path, path_args=path_args, **{self._ENTRY_CLASS.IDNAME: i['id']}
                )
            )
        super().__init__(data)
