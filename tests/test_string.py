#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import unittest

from tocoli.string import *

hello = u'Hello'
world = u'World'

class Tests(unittest.TestCase):


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


    # @unittest.skip("skip this test")
    def test_count_equal_chars(self):

        self.assertRaises(TypeError, count_equal_chars, None, None)

        res = count_equal_chars('', '')
        self.assertEqual(res, 0)

        res = count_equal_chars('a', 'b')
        self.assertEqual(res, 0)

        res = count_equal_chars('a', 'a')
        self.assertEqual(res, 1)

        res = count_equal_chars(u'a', u'a')
        self.assertEqual(res, 1)

        res = count_equal_chars(hello, world)
        self.assertEqual(res, 2)

        res = count_equal_chars(world, hello)
        self.assertEqual(res, 2)


    # @unittest.skip("skip this test")
    def test_strip_accents(self):

        res = strip_accents(u'áíóäöü')
        self.assertEqual(res, u'aioaou')


if __name__ == '__main__':
    unittest.main()
