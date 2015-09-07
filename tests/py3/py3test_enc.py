#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import unittest

from tocoli.py3.enc import *

b1 = b'Hello'
b2 = b'Hell\xc3\xb6'
u1 = 'Hello'
u2 = 'Hellö'

class TestStr(unittest.TestCase):

    # @unittest.skip("test_encode")
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

         # transformations
        res = encode(b'caf\xc3\xa9', input_encoding='utf-8', output_encoding='utf-8')
        self.assertEqual(res, b'caf\xc3\xa9')
        res = encode('café', input_encoding='utf-8', output_encoding='utf-8')
        self.assertEqual(res, b'caf\xc3\xa9')

        res = encode(b'caf\xc3\xa9', input_encoding='utf-8', output_encoding='latin-1')
        self.assertEqual(res, b'caf\xe9')
        res = encode('café', input_encoding='utf-8', output_encoding='latin-1')
        self.assertEqual(res, b'caf\xe9')

        res = encode(b'caf\xc3\xa9', input_encoding='utf-8', output_encoding='utf-16')
        self.assertEqual(res, b'\xff\xfec\x00a\x00f\x00\xe9\x00')
        res = encode('café', input_encoding='utf-8', output_encoding='utf-16')
        self.assertEqual(res, b'\xff\xfec\x00a\x00f\x00\xe9\x00')

        res = encode(b'caf\xc3\xa9', input_encoding='utf-8', output_encoding='utf-32')
        self.assertEqual(res, b'\xff\xfe\x00\x00c\x00\x00\x00a\x00\x00\x00f\x00\x00\x00\xe9\x00\x00\x00')
        res = encode('café', input_encoding='utf-8', output_encoding='utf-32')
        self.assertEqual(res, b'\xff\xfe\x00\x00c\x00\x00\x00a\x00\x00\x00f\x00\x00\x00\xe9\x00\x00\x00')

        res = encode(b'caf\xc3\xa9', input_encoding='utf-8', output_encoding='base64')
        self.assertEqual(res, b'Y2Fmw6k=\n')
        res = encode('café', input_encoding='utf-8', output_encoding='base64')
        self.assertEqual(res, b'Y2Fmw6k=\n')

        res = encode(b'Y2Fmw6k=\n', input_encoding='base64', output_encoding='utf-8')
        self.assertEqual(res, b'caf\xc3\xa9')
        res = encode('Y2Fmw6k=\n', input_encoding='base64', output_encoding='utf-8')
        self.assertEqual(res, b'caf\xc3\xa9')

        res = encode(b'Y2Fmw6k=\n', input_encoding='base64', output_encoding='utf-16')
        self.assertEqual(res, b'\xff\xfec\x00a\x00f\x00\xe9\x00')
        res = encode('Y2Fmw6k=\n', input_encoding='base64', output_encoding='utf-16')
        self.assertEqual(res, b'\xff\xfec\x00a\x00f\x00\xe9\x00')

        res = encode(b'Y2Fmw6k=\n', input_encoding='base64', output_encoding='latin-1')
        self.assertEqual(res, b'caf\xe9')
        res = encode('Y2Fmw6k=\n', input_encoding='base64', output_encoding='latin-1')
        self.assertEqual(res, b'caf\xe9')

        res = encode(b'\xff\xfec\x00a\x00f\x00\xe9\x00', input_encoding='utf-16', output_encoding='utf-32')
        self.assertEqual(res, b'\xff\xfe\x00\x00c\x00\x00\x00a\x00\x00\x00f\x00\x00\x00\xe9\x00\x00\x00')
        res = encode('\xff\xfec\x00a\x00f\x00\xe9\x00', input_encoding='utf-16', output_encoding='utf-32')
        self.assertEqual(res, b'\xff\xfe\x00\x00c\x00\x00\x00a\x00\x00\x00f\x00\x00\x00\xe9\x00\x00\x00')

        res = encode(b'\xff\xfe\x00\x00c\x00\x00\x00a\x00\x00\x00f\x00\x00\x00\xe9\x00\x00\x00', input_encoding='utf-32', output_encoding='utf-16')
        self.assertEqual(res, b'\xff\xfec\x00a\x00f\x00\xe9\x00')
        res = encode('\xff\xfe\x00\x00c\x00\x00\x00a\x00\x00\x00f\x00\x00\x00\xe9\x00\x00\x00', input_encoding='utf-32', output_encoding='utf-16')
        self.assertEqual(res, b'\xff\xfec\x00a\x00f\x00\xe9\x00')

        # exceptions
        self.assertRaises(UnicodeEncodeError, encode, b'caf\xc3\xa9', input_encoding='utf-8', output_encoding='ascii')
        self.assertRaises(UnicodeEncodeError, encode, 'café', input_encoding='utf-8', output_encoding='ascii')

        self.assertRaises(UnicodeEncodeError, encode, b'Y2Fmw6k=\n', input_encoding='base64', output_encoding='ascii')
        self.assertRaises(UnicodeEncodeError, encode, 'Y2Fmw6k=\n', input_encoding='base64', output_encoding='ascii')


    # @unittest.skip("test_decode")
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

         # transformations
        res = decode(b'caf\xc3\xa9', encoding='utf-8')
        self.assertEqual(res, 'café')
        res = decode('café', encoding='utf-8')
        self.assertEqual(res, 'café')

        res = decode(b'\xff\xfec\x00a\x00f\x00\xe9\x00', encoding='utf-16')
        self.assertEqual(res, 'café')
        res = decode('\xff\xfec\x00a\x00f\x00\xe9\x00', encoding='utf-16')
        self.assertEqual(res, 'café')

        res = decode(b'\xff\xfe\x00\x00c\x00\x00\x00a\x00\x00\x00f\x00\x00\x00\xe9\x00\x00\x00', encoding='utf-32')
        self.assertEqual(res, 'café')
        res = decode('\xff\xfe\x00\x00c\x00\x00\x00a\x00\x00\x00f\x00\x00\x00\xe9\x00\x00\x00', encoding='utf-32')
        self.assertEqual(res, 'café')

        res = decode(b'Y2Fmw6k=\n', encoding='base64')
        self.assertEqual(res, 'café')
        res = decode('Y2Fmw6k=\n', encoding='base64')
        self.assertEqual(res, 'café')

        res = decode(b'caf\xe9', 'latin-1')
        self.assertEqual(res, 'café')
        res = decode('caf\xe9', 'latin-1')
        self.assertEqual(res, 'café')

        res = decode(b'//5jAGEAZgDpAA==\n', 'base64', detect='utf-16')
        self.assertEqual(res, 'café')
        res = decode('//5jAGEAZgDpAA==\n', 'base64', detect='utf-16')
        self.assertEqual(res, 'café')

        res = decode(b'//4AAGMAAABhAAAAZgAAAOkAAAA=\n', 'base64', detect='utf-32')
        self.assertEqual(res, 'café')
        res = decode('//4AAGMAAABhAAAAZgAAAOkAAAA=\n', 'base64', detect='utf-32')
        self.assertEqual(res, 'café')

        # auto detect encoding
        res = decode(b'//5jAGEAZgDpAA==\n', 'base64')
        self.assertEqual(res, 'café')
        res = decode('//5jAGEAZgDpAA==\n', 'base64')
        self.assertEqual(res, 'café')

        res = decode(b'//4AAGMAAABhAAAAZgAAAOkAAAA=\n', 'base64')
        self.assertEqual(res, 'café')
        res = decode('//4AAGMAAABhAAAAZgAAAOkAAAA=\n', 'base64')
        self.assertEqual(res, 'café')

    # @unittest.skip("test_encoding_composition")
    def test_encoding_composition(self):

        self.assertEqual(decode(encode(b'caf\xc3\xa9')), 'café')
        self.assertEqual(decode(encode('café')), 'café')

        self.assertEqual(decode(encode(b'caf\xc3\xa9', 'base64'), 'base64'), 'café')
        self.assertEqual(decode(encode('café', 'base64'), 'base64'), 'café')

        self.assertEqual(decode(encode(b'caf\xc3\xa9', 'latin-1'), 'latin-1'), 'café')
        self.assertEqual(decode(encode('café', 'latin-1'), 'latin-1'), 'café')

        self.assertEqual(decode(encode(b'Y2Fmw6k=', 'utf-16', input_encoding='base64'), 'utf-16'), 'café')
        self.assertEqual(decode(encode('café', 'utf-16'), 'utf-16'), 'café')

        self.assertEqual(decode(encode(b'caf\xc3\xa9', 'utf-32'), 'utf-32'), 'café')
        self.assertEqual(decode(encode('café', 'utf-32'), 'utf-32'), 'café')

if __name__ == '__main__':
    unittest.main()
