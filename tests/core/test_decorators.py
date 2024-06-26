import unittest
from unittest import mock

import pytest
from pyramid.httpexceptions import HTTPOk
from pyramid.response import Response

from kinto.core.decorators import cache_forever


@cache_forever
def demo1(request):
    request.mock()
    return "demo1"


@cache_forever
def demo2(request, name):
    return "demo2: {}".format(name)


@cache_forever
def demo3(request):
    return request.response

class TestCacheForever(unittest.TestCase):

    def test_cache_forever_saves_result_and_updates_headers(self):
        request = mock.MagicMock()
        request.response = Response()
        demo1(request)
        assert cache_forever.coverage_data_call["branch 1"] > 0
        assert cache_forever.coverage_data_call["branch 3"] > 0

    def test_cache_forever_raises_value_error_for_response(self):
        request = mock.MagicMock()
        request.response = HTTPOk()
        with pytest.raises(ValueError, match="cache_forever cannot cache Response only its body"):
            demo3(request)
        assert cache_forever.coverage_data_call["branch 1"] > 0
        assert cache_forever.coverage_data_call["branch 2"] > 0

    def test_cache_forever_uses_cached_result(self):
        request = mock.MagicMock()
        request.response = Response()
        demo1(request)
        demo1(request)
        assert cache_forever.coverage_data_call["branch 4"] > 0

    def test_cache_forever_decorator_call_the_decorated_function_once():
        request = mock.MagicMock()
        demo1(request)
        demo1(request)
        demo1(request)
        assert request.mock.call_count == 1


    def test_cache_forever_doesnt_care_about_arguments():
        request1 = mock.MagicMock()
        request1.response = Response()

        request2 = mock.MagicMock()
        request2.response = Response()

        response1 = demo2(request1, "Henri").text
        response2 = demo2(request2, "Paul").text
        assert response1 == response2 == "demo2: Henri"


    def test_each_function_is_cached_separately_for_the_life_of_the_process():
        request1 = mock.MagicMock()
        request1.response = Response()
        response1 = demo1(request1).text

        request2 = mock.MagicMock()
        request2.response = Response()
        response2 = demo2(request2).text

        assert response1 != response2
        assert response1 == "demo1"
        assert response2 == "demo2: Henri"


    def test_should_not_cache_responses():
        request = mock.MagicMock()
        request.response = HTTPOk()

        with pytest.raises(ValueError):
            demo3(request)


if __name__ == "__main__":
    unittest.main()