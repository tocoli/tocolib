#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import unittest
import codecs

from tocoli.enc import *

b_ascii   = codecs.encode(u'hello', 'ascii')
u_ascii   = codecs.decode(b_ascii, 'ascii')

b_latin_1 = codecs.encode(u'café', 'latin-1')
u_latin_1 = codecs.decode(b_latin_1, 'latin-1')

b_utf_8   = codecs.encode(u'café', 'utf-8')
u_utf_8   = codecs.decode(b_utf_8, 'utf-8')

b_utf_16  = codecs.encode(u'café', 'utf-16')
u_utf_16  = codecs.decode(b_utf_16, 'utf-16')

b_utf_32  = codecs.encode(u'café', 'utf-32')
u_utf_32  = codecs.decode(b_utf_32, 'utf-32')

b_base64  = codecs.encode(b_utf_8, 'base64')
u_base64  = codecs.decode(b_base64, 'base64')


class TestEncoding(unittest.TestCase):

    def test_encode_decode(self):

        # ascii
        self.assertEqual(encode(u_ascii, 'ascii'), b_ascii)
        self.assertEqual(decode(b_ascii), u_ascii)
        self.assertEqual(encode(decode(b_ascii), 'ascii'), b_ascii)
        self.assertEqual(decode(encode(u_ascii, 'ascii')), u_ascii)

        # latin-1
        self.assertEqual(encode(u_latin_1, 'latin-1'), b_latin_1)
        self.assertEqual(decode(b_latin_1), u_latin_1)
        self.assertEqual(encode(decode(b_latin_1), 'latin-1'), b_latin_1)
        self.assertEqual(decode(encode(u_latin_1, 'latin-1')), u_latin_1)

        # utf-8
        self.assertEqual(encode(u_utf_8), b_utf_8)
        self.assertEqual(decode(b_utf_8), u_utf_8)
        self.assertEqual(encode(decode(b_utf_8)), b_utf_8)
        self.assertEqual(decode(encode(u_utf_8)), u_utf_8)

        # utf-16
        self.assertEqual(encode(u_utf_16, 'utf-16'), b_utf_16)
        self.assertEqual(decode(b_utf_16), u_utf_16)
        self.assertEqual(encode(decode(b_utf_16), 'utf-16'), b_utf_16)
        self.assertEqual(decode(encode(u_utf_16, 'utf-16')), u_utf_16)

        # utf-32
        self.assertEqual(encode(u_utf_32, 'utf-32'), b_utf_32)
        self.assertEqual(decode(b_utf_32), u_utf_32)
        self.assertEqual(encode(decode(b_utf_32), 'utf-32'), b_utf_32)
        self.assertEqual(decode(encode(u_utf_32, 'utf-32')), u_utf_32)

        # base64
        self.assertEqual(encode(u_utf_8, 'base64'), b_base64)
        self.assertEqual(decode(b_base64, 'base64'), u_utf_8)
        self.assertEqual(encode(decode(b_base64, 'base64'), 'base64'), b_base64)
        self.assertEqual(decode(encode(u_utf_8, 'base64'), 'base64'), u_utf_8)
