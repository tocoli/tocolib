#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import unittest

from tocoli.py3.str import *

b1 = str.encode('Hello')
b2 = str.encode('Hellö')
u1 = 'Hello'
u2 = 'Hellö'

class TestStr(unittest.TestCase):

    def test_decode(self):

        # apply
        self.assertEqual(type(decode(b1)), str)
        self.assertEqual(type(decode(b2)), str)
        self.assertEqual(type(decode(u1)), str)
        self.assertEqual(type(decode(u2)), str)

        self.assertEqual(decode(b1), u1)
        self.assertEqual(decode(b2), u2)
        self.assertEqual(decode(u1), u1)
        self.assertEqual(decode(u2), u2)

        # don't apply
        self.assertEqual(decode(0), 0)
        self.assertEqual(decode(1), 1)
        self.assertEqual(decode(0.0), 0.0)
        self.assertEqual(decode(1.1), 1.1)
        self.assertEqual(decode(True), True)
        self.assertEqual(decode(False), False)
        self.assertEqual(decode(None), None)

    def test_encode(self):

        # apply
        self.assertEqual(type(encode(b1)), bytes)
        self.assertEqual(type(encode(b2)), bytes)
        self.assertEqual(type(encode(u1)), bytes)
        self.assertEqual(type(encode(u2)), bytes)

        self.assertEqual(encode(b1), b1)
        self.assertEqual(encode(b2), b2)
        self.assertEqual(encode(u1), b1)
        self.assertEqual(encode(u2), b2)

        # don't apply
        self.assertEqual(encode(0), 0)
        self.assertEqual(encode(1), 1)
        self.assertEqual(encode(0.0), 0.0)
        self.assertEqual(encode(1.1), 1.1)
        self.assertEqual(encode(True), True)
        self.assertEqual(encode(False), False)
        self.assertEqual(encode(None), None)
