#!/usr/bin/env python3
'''
Unittests and Integration Tests
'''
from importlib.resources import path
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    '''
    Access Nested Map Testing Class
    '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), ({"b": 2})),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        ''' Tests that the expected output is returned '''
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
        # ({"a": {"b": 2}}, ("a",), ({"b": 2})),
        # ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map_exception(self, nested_map,
                                         path, expected_result):
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual("KeyError('{}')".format(expected_result),
                         repr(e.exception))


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        with patch('requests.get') as mock_request:
            mock_request.return_value = Mock(**{"json.return_value": test_payload})
            self.assertEqual(get_json(test_url), test_payload)
            mock_request.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    '''

    '''
    def test_memoize(self):
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_memoize:
            test_class = TestClass()
            mock_memoize.return_value = lambda: 42
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            mock_memoize.assert_called_once()
