#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import unittest

from tocoli.filter import *
# from tocoli import filter

strings = [u'Hello', u'hello', u'ello', u'Bello', u'schnello', u'world']

class TestFilters(unittest.TestCase):

    # @unittest.skip("skip this test")
    def test_filter_strings_by_similarity(self):

        res = filter_strings_by_similarity(strings, [u'Hello'])
        self.assertEqual(res, [u'Hello', u'hello', u'ello'])

        res = filter_strings_by_similarity(strings, [u'Hello', u'World'])
        self.assertEqual(res, [u'Hello', u'hello', u'ello', u'world'])

        res = filter_strings_by_similarity(strings, [u'Hello', u'Wörld'])
        self.assertEqual(res, [u'Hello', u'hello', u'ello', u'world'])

        res = filter_strings_by_similarity(strings, [u'Hello', u'Wörld'], case_sensitive=True)
        self.assertEqual(res, [u'Hello', u'ello'])


    # @unittest.skip("skip this test")
    def test_filter_strings_by_keywords(self):

        res = filter_strings_by_keywords(strings, [u'Hello'])
        self.assertEqual(res, [u'Hello', u'hello'])

        res = filter_strings_by_keywords(strings, [u'Hello'], case_sensitive=True)
        self.assertEqual(res, [u'Hello'])


    # @unittest.skip("skip this test")
    def test_filter_dicts_by_keys(self):

        dicts = [{1: 'one'}, {2: 'two'}, {2: 'two', 3: 'three'}, {4: 'four'}]

        res = filter_dicts_by_keys(dicts, [1])
        self.assertEqual(res, [{1: 'one'}])

        res = filter_dicts_by_keys(dicts, [2])
        self.assertEqual(res, [{2: 'two'}, {2: 'two', 3: 'three'}])

        res = filter_dicts_by_keys(dicts, [3])
        self.assertEqual(res, [{2: 'two', 3: 'three'}])

        res = filter_dicts_by_keys(dicts, [4])
        self.assertEqual(res, [{4: 'four'}])

        res = filter_dicts_by_keys(dicts, [1, 4])
        self.assertEqual(res, [{1: 'one'}, {4: 'four'}])


    # @unittest.skip("skip this test")
    def test_filter_dicts_by_values(self):

        dicts = [{1: 'one'}, {2: 'two'}, {2: 'two', 3: 'three'}, {4: 'four'}]

        res = filter_dicts_by_values(dicts, ['two'])
        self.assertEqual(res, [{2: 'two'}, {2: 'two', 3: 'three'}])


    # @unittest.skip("skip this test")
    def test_filter_bytes(self):
        from tocoli import PY2
        res = filter_bytes('hello', lambda x: x == 'l')
        if PY2:
            self.assertEqual(res, 'll')
        else:
            self.assertEqual(res, b'll')

    # @unittest.skip("skip this test")
    def test_filter_string(self):
        res = filter_string('hello', lambda x: x == 'l')
        self.assertEqual(res, 'll')

        res = filter_string(u'hello', lambda x: x == 'l')
        self.assertEqual(res, u'll')

    # @unittest.skip("skip this test")
    def test_filter_iter(self):
        res = filter_iter(iter([1, 2]), lambda x: x == 1)
        self.assertEqual(res, [1])

    # @unittest.skip("skip this test")
    def test_filter_list(self):
        res = filter_list([1, 2], lambda x: x == 1)
        self.assertEqual(res, [1])

    # @unittest.skip("skip this test")
    def test_filter_tuple(self):
        res = filter_tuple((1, 2), lambda x: x == 1)
        self.assertEqual(res, [1])

    # @unittest.skip("skip this test")
    def test_filter_set(self):
        res = filter_set({1, 2}, lambda x: x == 1)
        self.assertEqual(res, {1})

    # @unittest.skip("skip this test")
    def test_filter_dict_by_key(self):
        res = filter_dict_by_key({1: 'one', 2: 'two'}, [1])
        self.assertEqual(res, {1: 'one', 2: 'two'})

        res = filter_dict_by_key({1: 'one', 2: 'two'}, [3])
        self.assertEqual(res, None)

    # @unittest.skip("skip this test")
    def test_filter_dict_by_value(self):
        res = filter_dict_by_value({1: 'one', 2: 'two'}, ['one'])
        self.assertEqual(res, {1: 'one', 2: 'two'})

        res = filter_dict_by_value({1: 'one', 2: 'two'}, ['three'])
        self.assertEqual(res, None)

    # @unittest.skip("skip this test")
    def test_clean(self):

        res = clean('1.20€')
        self.assertEqual(res, '120')

        res = clean('1.20€', '.')
        self.assertEqual(res, '1.20')

        res = clean('1.20€', '.€')
        self.assertEqual(res, '1.20€')

        res = clean('Hello', alpha='a-z')
        self.assertEqual(res, 'ello')

        res = clean('áíóäöü', 'áíóäöü')
        self.assertEqual(res, 'áíóäöü')


if __name__ == '__main__':
    unittest.main()
