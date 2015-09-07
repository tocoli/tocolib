#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import unittest

hello = u'Hello'
world = u'World'

class Tests(unittest.TestCase):


    # @unittest.skip("skip this test")
    def test_join_strings_by_keywords(self):
        from tocoli.join import join_strings_by_keywords

        res = join_strings_by_keywords('Hello World'.split(), ['do not join anything'])
        self.assertEqual(res, ['Hello', 'World'])

        res = join_strings_by_keywords('Hello and World'.split(), keywords=['and'])
        self.assertEqual(res, ['Hello World'])

        res = join_strings_by_keywords('Hello AND World'.split(), keywords=['and'])
        self.assertEqual(res, ['Hello World'])

        res = join_strings_by_keywords('Hello  +  World'.split(), keywords=['+', '-'])
        self.assertEqual(res, ['Hello World'])

        res = join_strings_by_keywords('Hello  -  World'.split(), keywords=['+', '-'])
        self.assertEqual(res, ['Hello World'])

        res = join_strings_by_keywords(' - Hello + World'.split(), keywords=['+', '-'])
        self.assertEqual(res, ['Hello World'])

        res = join_strings_by_keywords('Hello + World - '.split(), keywords=['+', '-'])
        self.assertEqual(res, ['Hello World'])

        res = join_strings_by_keywords(' - Hello + World - '.split(), keywords=['+', '-'])
        self.assertEqual(res, ['Hello World'])

        res = join_strings_by_keywords('one + two + three + four'.split(), keywords=['+', '-'])
        self.assertEqual(res, ['one two three four'])

        res = join_strings_by_keywords('áíó äöü'.split(), ['do not join anything'])
        self.assertEqual(res, ['áíó', 'äöü'])

        res = join_strings_by_keywords('áíó and äöü'.split(), keywords=['and'])
        self.assertEqual(res, ['áíó äöü'])
