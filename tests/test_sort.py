#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from tocoli.sort import *
from tocoli import sort


class TestSort(unittest.TestCase):

    # @unittest.skip("skip this test")
    def test_sort_dicts(self):

        # Simple sort by a key
        dicts = [{'name': 'Eve'},
                 {'name': 'Alice', 'email': 'alice@example.com'},
                 {'email': 'bob@example.com', 'name': 'Bob'}]

        res = sort_dicts_by_value(dicts, ['name'])
        self.assertEqual(res, [{'name': 'Alice', 'email': 'alice@example.com'},
                               {'email': 'bob@example.com', 'name': 'Bob'},
                               {'name': 'Eve'}])


        dicts = [{'firstname': 'Bob',   'lastname': 'Abel'},
                 {'firstname': 'Alice', 'lastname': 'Bond'},
                 {'firstname': 'Carol', 'lastname': 'Bond'},
                 {'firstname': 'Bob',   'lastname': 'Bond'},
                 {'firstname': 'Carol', 'lastname': 'Abel'},
                 {'firstname': 'Alice', 'lastname': 'Abel'}]

        res = sort_dicts_by_value(dicts, ['lastname', 'firstname'])
        self.assertEqual(res, [{'firstname': 'Alice', 'lastname': 'Abel'},
                               {'firstname': 'Bob',   'lastname': 'Abel'},
                               {'firstname': 'Carol', 'lastname': 'Abel'},
                               {'firstname': 'Alice', 'lastname': 'Bond'},
                               {'firstname': 'Bob',   'lastname': 'Bond'},
                               {'firstname': 'Carol', 'lastname': 'Bond'}])

        # Advanced sort for multiple keys with custom sort value:

        dicts = [{'price': 100},
                 {'price': 50, 'shipping': 40},
                 {'shipping': 5, 'price': 55}]

        def total(price, shipping):
            return price + shipping

        res = sort_dicts_by_value(dicts,
                         ['price', 'shipping'],
                         values=total,
                         default=0,
                         sequentially=False)

        self.assertEqual(res, [{'price': 55, 'shipping': 5},
                               {'price': 50, 'shipping': 40},
                               {'price': 100}])


        # Sort dictionaries with non string keys:

        dicts = [{1: False},
                 {'right': True, 1: False},
                 {1: True, 'right': True}]

        def both(left, right):
            return left and right

        res = sort_dicts_by_value(
            dicts,
            [{'key': 1, 'alias': 'left'}, 'right'],
            values=both,
            default=False,
            sequentially=False,
            reverse=True)

        self.assertEqual(res, [{1: True, 'right': True},
                               {1: False},
                               {1: False, 'right': True}])


        dicts = [{'a': 1, 'b': 4},
                 {'a': 2, 'b': 3},
                 {'a': 1, 'b': 2},
                 {'a': 2, 'b': 1},
                 {'a': 4, 'b': 1},
                 {'a': 3, 'b': 1}]

        res = sort_dicts_by_value(dicts, ['b', 'a'])
        self.assertEqual(res, [{'a': 2, 'b': 1},
                               {'a': 3, 'b': 1},
                               {'a': 4, 'b': 1},
                               {'a': 1, 'b': 2},
                               {'a': 2, 'b': 3},
                               {'a': 1, 'b': 4}])


        res = sort_dicts_by_value(dicts, ['b', 'a'], reverse=True)
        self.assertEqual(res, [{'a': 1, 'b': 4},
                               {'a': 2, 'b': 3},
                               {'a': 1, 'b': 2},
                               {'a': 4, 'b': 1},
                               {'a': 3, 'b': 1},
                               {'a': 2, 'b': 1}])


        res = sort_dicts_by_value(dicts, ['b', {'key': 'a', 'sort': ASCENDING}])
        self.assertEqual(res, [{'a': 2, 'b': 1},
                               {'a': 3, 'b': 1},
                               {'a': 4, 'b': 1},
                               {'a': 1, 'b': 2},
                               {'a': 2, 'b': 3},
                               {'a': 1, 'b': 4}])

        res = sort_dicts_by_value(dicts, ['b', {'key': 'a', 'sort': DESCENDING}])
        self.assertEqual(res, [{'a': 4, 'b': 1},
                               {'a': 3, 'b': 1},
                               {'a': 2, 'b': 1},
                               {'a': 1, 'b': 2},
                               {'a': 2, 'b': 3},
                               {'a': 1, 'b': 4}])

        dicts = [{'a': 1, 'b': 4},
                 {'a': 2, 'b': 3},
                 {'a': 1, 'b': 2},
                 {'a': 2, 'b': 1},
                 {'a': 4, 'b': 1},
                 {'a': 3, 'b': 1}]


    # @unittest.skip("skip this test")
    def test_sort_dicts_by_similarity(self):

        dicts = [{'word': u'schnello'},
                 {'word': u'bello'},
                 {'word': u'ello'},
                 {'word': u'Hello'},
                 {'word': u'hello'},
                 {'word': u'trello'}]

        res = sort_dicts_by_similarity(dicts, u'hello', ['word'])
        self.assertEqual(res, [{'word': u'Hello'},
                               {'word': u'hello'},
                               {'word': u'ello'},
                               {'word': u'bello'},
                               {'word': u'schnello'},
                               {'word': u'trello'}])

        res = sort_dicts_by_similarity(dicts, u'hello', ['word'], reverse=True)
        self.assertEqual(res,[{'word': u'trello'},
                               {'word': u'schnello'},
                               {'word': u'bello'},
                               {'word': u'ello'},
                               {'word': u'Hello'},
                               {'word': u'hello'}])


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

        res = sort_dict_by_key({3: 'a', 4: 'c', 1: 'b', 2: 'd'}, reverse=True)
        self.assertEqual(res, [(4, 'c'), (3, 'a'), (2, 'd'), (1, 'b')])

    # @unittest.skip("skip this test")
    def test_sort_dict_by_values(self):

        res = sort_dict_by_value({3: 'a', 4: 'c', 1: 'b', 2: 'd'})
        self.assertEqual(res, [(3, 'a'), (1, 'b'), (4, 'c'), (2, 'd')])

        res = sort_dict_by_value({3: 'a', 4: 'c', 1: 'b', 2: 'd'}, reverse=True)
        self.assertEqual(res, [(2, 'd'), (4, 'c'), (1, 'b'), (3, 'a')])


    # @unittest.skip("skip this test")
    def test_sort_bytes(self):
        from tocoli import PY2

        res = sort_bytes('hello')
        if PY2:
            self.assertEqual(res, 'ehllo')
        else:
            self.assertEqual(res, b'ehllo')

        res = sort_bytes(u'hello')
        if PY2:
            self.assertEqual(res, 'ehllo')
        else:
            self.assertEqual(res, b'ehllo')

    # @unittest.skip("skip this test")
    def test_sort_string(self):
        res = sort_string('hello')
        self.assertEqual(res, 'ehllo')

        res = sort_string(u'hellö')
        self.assertEqual(res, u'ehllö')

    # @unittest.skip("skip this test")
    def test_sort_iter(self):
        res = sort_iter(iter(['b', 'a', 'c']))
        self.assertEqual(res, ['a', 'b', 'c'])

    # @unittest.skip("skip this test")
    def test_sort_list(self):
        res = sort_list(['b', 'a', 'c'])
        self.assertEqual(res, ['a', 'b', 'c'])

    # @unittest.skip("skip this test")
    def test_sort_tuple(self):
        res = sort_tuple((1, 3, 2))
        self.assertEqual(res, [1, 2, 3])

    # @unittest.skip("skip this test")
    def test_sort_set(self):
        res = sort_set(set([1, 3, 2, 3, 2]))
        self.assertEqual(res, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
