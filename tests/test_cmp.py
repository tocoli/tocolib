#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from tocoli.cmp import *


strings = [u'Hello', u'hello', u'ello', u'Bello', u'schnello', u'world']


class Tests(unittest.TestCase):

    # @unittest.skip("skip this test")
    def test_comparable(self):

        # strings
        s1 = u'Hello'
        s2 = u'hello'

        left, right = comparable(s1, s2)
        self.assertEqual(left, u'hello')
        self.assertEqual(right, u'hello')

        left, right = comparable(s1, s2, case_sensitive=True)
        self.assertEqual(left, u'Hello')
        self.assertEqual(right, u'hello')

        # lists
        l1 = [u'A', u'B']
        l2 = [u'a', u'b']

        left, right = comparable(l1, l2)
        self.assertEqual(left, [u'a', u'b'])
        self.assertEqual(right, [u'a', u'b'])

        left, right = comparable(l1, l2, case_sensitive=True)
        self.assertEqual(left, [u'A', u'B'])
        self.assertEqual(right, [u'a', u'b'])

if __name__ == '__main__':
    unittest.main()
