#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from tocoli import PY2

from tocoli.type import *
from tocoli import type


class Tests(unittest.TestCase):

    # @unittest.skip("skip this test")
    def test_to_bool(self):

        self.assertEqual(to_bool(True), True)
        self.assertEqual(to_bool('True'), True)
        self.assertEqual(to_bool('true'), True)
        self.assertEqual(to_bool('Yes'), True)
        self.assertEqual(to_bool('yes'), True)
        self.assertEqual(to_bool('Y'), True)
        self.assertEqual(to_bool('y'), True)
        self.assertEqual(to_bool(u'True'), True)
        self.assertEqual(to_bool(u'true'), True)
        self.assertEqual(to_bool(u'Yes'), True)
        self.assertEqual(to_bool(u'yes'), True)
        self.assertEqual(to_bool(u'Y'), True)
        self.assertEqual(to_bool(u'y'), True)
        self.assertEqual(to_bool('1'), True)
        self.assertEqual(to_bool('2'), True)
        # ...
        self.assertEqual(to_bool(1), True)
        self.assertEqual(to_bool(2), True)
        # ...

        self.assertEqual(to_bool(False), False)
        self.assertEqual(to_bool(None), False)
        self.assertEqual(to_bool(0), False)
        self.assertEqual(to_bool(''), False)
        self.assertEqual(to_bool('0'), False)
        self.assertEqual(to_bool('False'), False)
        self.assertEqual(to_bool('false'), False)
        self.assertEqual(to_bool('No'), False)
        self.assertEqual(to_bool('no'), False)
        self.assertEqual(to_bool('N'), False)
        self.assertEqual(to_bool('n'), False)
        self.assertEqual(to_bool('bullshit'), False)
        # ...
        self.assertEqual(to_bool(u'False'), False)
        self.assertEqual(to_bool(u'false'), False)
        self.assertEqual(to_bool(u'No'), False)
        self.assertEqual(to_bool(u'no'), False)
        self.assertEqual(to_bool(u'N'), False)
        self.assertEqual(to_bool(u'n'), False)
        self.assertEqual(to_bool(u'bullshit'), False)
        # ...


    # @unittest.skip("skip this test")
    def test_to_integer(self):

        self.assertEqual(to_integer(1), 1)

        self.assertEqual(to_integer('0'), 0)
        self.assertEqual(to_integer('1'), 1)
        self.assertEqual(to_integer('2'), 2)
        self.assertEqual(to_integer('3'), 3)
        self.assertEqual(to_integer('4'), 4)
        self.assertEqual(to_integer('5'), 5)
        self.assertEqual(to_integer('6'), 6)
        self.assertEqual(to_integer('7'), 7)
        self.assertEqual(to_integer('8'), 8)
        self.assertEqual(to_integer('9'), 9)
        self.assertEqual(to_integer('10'), 10)

        self.assertEqual(to_integer('zero'), 0)
        self.assertEqual(to_integer('one'), 1)
        self.assertEqual(to_integer('two'), 2)
        self.assertEqual(to_integer('three'), 3)
        self.assertEqual(to_integer('four'), 4)
        self.assertEqual(to_integer('five'), 5)
        self.assertEqual(to_integer('six'), 6)
        self.assertEqual(to_integer('seven'), 7)
        self.assertEqual(to_integer('eight'), 8)
        self.assertEqual(to_integer('nine'), 9)
        self.assertEqual(to_integer('ten'), 10)


if __name__ == '__main__':
    unittest.main()
