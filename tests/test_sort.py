#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import unittest

from tocoli.sort import *
from tocoli import sort


class Tests(unittest.TestCase):

    # @unittest.skip("skip this test")
    def test_sort_dicts(self):

        # Simple sort by a key
        dicts = [{'name': 'Eve'},
                 {'name': 'Alice', 'email': 'alice@example.com'},
                 {'email': 'bob@example.com', 'name': 'Bob'}]

        res = sort_dicts_by_value(dicts, ['name'])
        self.assertEqual(res,
                         [{'name': 'Alice', 'email': 'alice@example.com'},
                          {'email': 'bob@example.com', 'name': 'Bob'},
                          {'name': 'Eve'}])


        # Advanced sort for multiple keys with custom sort value:

        dicts = [{'price': 100},
                 {'price': 50, 'shipping': 40},
                 {'shipping': 5, 'price': 55}]

        def total(price, shipping):
            return price + shipping

        res = sort_dicts_by_value(dicts,
                         ['price', 'shipping'],
                         values=total,
                         default=0)

        self.assertEqual(res, [{'price': 55, 'shipping': 5},
                               {'price': 50, 'shipping': 40},
                               {'price': 100}])


        # Sort dictionaries with non string keys:

        dicts = [{1: False},
                 {2: True, 1: False},
                 {1: True, 2: True}]

        def both(left, right):
            return left and right

        res = sort_dicts_by_value(dicts,
                         {1: 'left', 2: 'right'},
                         values=both,
                         default=False,
                         reverse=True)

        self.assertEqual(res, [{1: True, 2: True},
                               {1: False},
                               {1: False, 2: True}])

    # @unittest.skip("skip this test")
    def test_sort_dicts_by_similarity(self):

        dicts = [{'word': 'schnello'},
                 {'word': 'bello'},
                 {'word': 'ello'},
                 {'word': 'Hello'},
                 {'word': 'hello'},
                 {'word': 'trello'}]

        res = sort_dicts_by_similarity(dicts, 'hello', ['word'])
        self.assertEqual(res, [{'word': 'trello'},
                               {'word': 'schnello'},
                               {'word': 'bello'},
                               {'word': 'ello'},
                               {'word': 'Hello'},
                               {'word': 'hello'}])

        res = sort_dicts_by_similarity(dicts, 'hello', ['word'], reverse=True)
        self.assertEqual(res, [{'word': 'Hello'},
                               {'word': 'hello'},
                               {'word': 'ello'},
                               {'word': 'bello'},
                               {'word': 'schnello'},
                               {'word': 'trello'}])


    # @unittest.skip("skip this test")
    def test_sort_strings_by_similarity(self):

        l = ['schnello', 'bello', 'ello', 'Hello', 'hello', 'trello']

        res = sort_strings_by_similarity(l, 'hello')
        self.assertEqual(res, ['trello', 'schnello', 'bello', 'ello', 'Hello', 'hello'])

        res = sort_strings_by_similarity(l, 'hello', reverse=True)
        self.assertEqual(res, ['Hello', 'hello', 'ello', 'bello', 'schnello', 'trello'])

        res = sort_strings_by_similarity(l, 'hello', reverse=True, weights=(1,0))
        self.assertEqual(res, ['Hello', 'hello', 'bello', 'ello', 'schnello', 'trello'])


    # @unittest.skip("skip this test")
    def test_sort_dict_by_keys(self):

        res = sort_dict_by_key({3: 'a', 4: 'c', 1: 'b', 2: 'd'})
        self.assertEqual(res, [(1, 'b'), (2, 'd'), (3, 'a'), (4, 'c')])

        res = sort_dict_by_key({3: 'a', 4: 'c', 1: 'b', 2: 'd'}, True)
        self.assertEqual(res, [(4, 'c'), (3, 'a'), (2, 'd'), (1, 'b')])

    # @unittest.skip("skip this test")
    def test_sort_dict_by_values(self):

        res = sort_dict_by_value({3: 'a', 4: 'c', 1: 'b', 2: 'd'})
        self.assertEqual(res, [(3, 'a'), (1, 'b'), (4, 'c'), (2, 'd')])

        res = sort_dict_by_value({3: 'a', 4: 'c', 1: 'b', 2: 'd'}, True)
        self.assertEqual(res, [(2, 'd'), (4, 'c'), (1, 'b'), (3, 'a')])


if __name__ == '__main__':
    unittest.main()
