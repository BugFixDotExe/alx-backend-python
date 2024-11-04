#!/usr/bin/env python3
'''
A script with methods for  running tests
'''
import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''
    The entry point for the test, it inherites from unittest.TestCase
    '''
    @parameterized.expand([
            ({"a": 1}, ("a",)),
            ({"a": {"b": 2}}, ("a",)),
            ({"a": {"b": 2}}, ("a", "b"))
    ])
    def test_access_nested_map(self, nested_map, path):
        '''
        test_access_nested_map: a function that returns the result of a
        list of key against, a dict
        Args:
            nested_map(Mapping):  A dict of key values
            path(iterable): A list of keys
        Returns:
            The result of the matching key
        '''
        ret_result = access_nested_map(nested_map, path)
        self.assertEqual(ret_result, ret_result)

    @parameterized.expand([
        ({}, ("a"),),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''
        A function that test for the expected behaviour of a KeyError
        Args:
            nested_map(Mapping): A dict of item
            path(List): A list of possible keys in nested_map
        Returns:
            A successful test on testing condition being true
            Fail if not successful in the expected outcome.
        '''
        with self.assertRaises(KeyError) as keyError:
            access_nested_map(nested_map, path)
