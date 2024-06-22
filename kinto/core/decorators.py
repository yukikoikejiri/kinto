import atexit
import threading
import warnings
from functools import update_wrapper, wraps

from pyramid.response import Response


class cache_forever:

    ### INSTRUMENTATION DATA STRUCTURE ###
    coverage_data_call = {
    "branch 1": 0, ##if self.saved is none
    "branch 2": 0, ##isinstance
    "branch 3": 0, ##first implicit else
    "branch 4": 0, ##second implicit else
    }


    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.saved = None
        self.saved_headers = None
        update_wrapper(self, wrapped)

    ### SELECTED FUNCTION ###
    def __call__(self, request, *args, **kwargs):
        if self.saved is None:
            ## BRANCH 1 ##
            cache_forever.coverage_data_call["branch 1"] += 1
            self.saved = self.wrapped(request, *args, **kwargs)
            self.saved_headers = request.response.headers
            if isinstance(self.saved, Response):
                ## BRANCH 1 ##
                cache_forever.coverage_data_call["branch 2"] += 1
                self.saved = None
                raise ValueError("cache_forever cannot cache Response only its body")
            else:
                ## BRANCH 2 ##
                cache_forever.coverage_data_call["branch 3"] += 1
        else:
            ## BRANCH 2 ##
            cache_forever.coverage_data_call["branch 4"] += 1

        request.response.write(self.saved)
        request.response.headers.update(**self.saved_headers)
        return request.response
    
    def print_coverage_data_call():
        print("Branch Coverage Report for function __call__:")
        print(f"Number of Branches: {len(cache_forever.coverage_data_call)}")
        total_executed = sum(1 for count in cache_forever.coverage_data_call.values() if count > 0)
        for branch, count in cache_forever.coverage_data_call.items():
            print(f"{branch}: executed {count} time(s)")
        coverage_percentage = (total_executed / len(cache_forever.coverage_data_call)) * 100
        print(f"Total Coverage: {coverage_percentage:.2f}% \n")


    atexit.register(print_coverage_data_call)


def synchronized(method):
    """Class method decorator to make sure two threads do not execute some code
    at the same time (c.f Java ``synchronized`` keyword).

    The decorator installs a mutex on the class instance.
    """

    @wraps(method)
    def decorated(self, *args, **kwargs):
        try:
            lock = getattr(self, "__lock__")
        except AttributeError:
            lock = threading.RLock()
            setattr(self, "__lock__", lock)

        lock.acquire()
        try:
            result = method(self, *args, **kwargs)
        finally:
            lock.release()
        return result

    return decorated


def deprecate_kwargs(deprecated):
    """
    A decorator to deprecate keyword arguments.

    :param dict deprecated: The keywords mapping (old: new)
    """

    def decorated(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_kwargs = {**kwargs}
            for old_param, new_param in deprecated.items():
                if old_param in kwargs:
                    message = f"{func.__qualname__} parameter {old_param!r} is deprecated, use {new_param!r} instead"
                    warnings.warn(message, DeprecationWarning)
                    new_kwargs[new_param] = new_kwargs.pop(old_param)

            return func(*args, **new_kwargs)

        return wrapper

    return decorated
