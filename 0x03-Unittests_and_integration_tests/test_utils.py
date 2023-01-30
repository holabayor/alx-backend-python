#!/usr/bin/env python3
'''
Unittests and Integration Tests
'''
from parameterized import parameterized
from utils import access_nested_map, get_json
import unittest


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
        self.assertEqual(get_json(test_url), test_payload)
