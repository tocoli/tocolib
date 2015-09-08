#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import unittest

from tocoli import PY2

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

    # @unittest.skip("skip this test")
    def test_join_values_as_string(self):
        from tocoli.join import join_values_as_string

        res = join_values_as_string(1, 2, 3)
        self.assertEqual(res, u'123')

        res = join_values_as_string(1, '2', 3.0)
        self.assertEqual(res, u'123.0')

        res = join_values_as_string(1, '2', 10 / 3.0)
        if PY2:
            self.assertEqual(res, u'123.33333333333')
        else:
            self.assertEqual(res, u'123.3333333333333335')


if __name__ == '__main__':
    unittest.main()
