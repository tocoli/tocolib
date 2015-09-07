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


if __name__ == '__main__':
    unittest.main()
