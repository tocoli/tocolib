#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
# import locale
# print locale.getpreferredencoding()
from tocoli.py2.enc import *

s1 = 'Hello'
s2 = 'Hellö'
u1 = u'Hello'
u2 = u'Hellö'

class TestStr(unittest.TestCase):

    # @unittest.skip("test_encode")
    def test_encode(self):

        # apply (utf-8)
        self.assertEqual(type(encode(s1)), str)
        self.assertEqual(type(encode(s2)), str)
        self.assertEqual(type(encode(u1)), str)
        self.assertEqual(type(encode(u2)), str)

        self.assertEqual(encode(s1), s1)
        self.assertEqual(encode(s2), s2)
        self.assertEqual(encode(u1), s1)
        self.assertEqual(encode(u2), s2)

        # don't apply
        self.assertEqual(encode(0), 0)
        self.assertEqual(encode(1), 1)
        self.assertEqual(encode(0.0), 0.0)
        self.assertEqual(encode(1.1), 1.1)
        self.assertEqual(encode(True), True)
        self.assertEqual(encode(False), False)
        self.assertEqual(encode(None), None)

        # transformations
        res = encode('café', output_encoding='utf-8', input_encoding='utf-8')
        self.assertEqual(res, 'café')
        res = encode(u'café', output_encoding='utf-8', input_encoding='utf-8')
        self.assertEqual(res, 'café')

        res = encode('café', output_encoding='utf-16', input_encoding='utf-8')
        self.assertEqual(res, '\xff\xfec\x00a\x00f\x00\xe9\x00')
        res = encode(u'café', output_encoding='utf-16', input_encoding='utf-8')
        self.assertEqual(res, '\xff\xfec\x00a\x00f\x00\xe9\x00')

        res = encode('café', output_encoding='utf-32', input_encoding='utf-8')
        self.assertEqual(res, '\xff\xfe\x00\x00c\x00\x00\x00a\x00\x00\x00f\x00\x00\x00\xe9\x00\x00\x00')
        res = encode(u'café', output_encoding='utf-32', input_encoding='utf-8')
        self.assertEqual(res, '\xff\xfe\x00\x00c\x00\x00\x00a\x00\x00\x00f\x00\x00\x00\xe9\x00\x00\x00')

        res = encode('café', output_encoding='base64', input_encoding='utf-8')
        self.assertEqual(res, 'Y2Fmw6k=\n')
        res = encode(u'café', output_encoding='base64', input_encoding='utf-8')
        self.assertEqual(res, 'Y2Fmw6k=\n')

        res = encode('Y2Fmw6k=\n', output_encoding='utf-8', input_encoding='base64')
        self.assertEqual(res, 'café')
        res = encode(u'Y2Fmw6k=\n', output_encoding='utf-8', input_encoding='base64')
        self.assertEqual(res, 'café')

        res = encode('Y2Fmw6k=\n', output_encoding='utf-16', input_encoding='base64')
        self.assertEqual(res, '\xff\xfec\x00a\x00f\x00\xe9\x00')
        res = encode(u'Y2Fmw6k=\n', output_encoding='utf-16', input_encoding='base64')
        self.assertEqual(res, '\xff\xfec\x00a\x00f\x00\xe9\x00')

        res = encode('Y2Fmw6k=\n', output_encoding='latin-1', input_encoding='base64')
        self.assertEqual(res, 'caf\xe9')
        res = encode(u'Y2Fmw6k=\n', output_encoding='latin-1', input_encoding='base64')
        self.assertEqual(res, 'caf\xe9')

        res = encode('\xff\xfec\x00a\x00f\x00\xe9\x00', output_encoding='utf-32', input_encoding='utf-16')
        self.assertEqual(res, '\xff\xfe\x00\x00c\x00\x00\x00a\x00\x00\x00f\x00\x00\x00\xe9\x00\x00\x00')
        res = encode(u'\xff\xfec\x00a\x00f\x00\xe9\x00', output_encoding='utf-32', input_encoding='utf-16')
        self.assertEqual(res, '\xff\xfe\x00\x00c\x00\x00\x00a\x00\x00\x00f\x00\x00\x00\xe9\x00\x00\x00')

        res = encode('\xff\xfe\x00\x00c\x00\x00\x00a\x00\x00\x00f\x00\x00\x00\xe9\x00\x00\x00', output_encoding='utf-16', input_encoding='utf-32')
        self.assertEqual(res, '\xff\xfec\x00a\x00f\x00\xe9\x00')
        res = encode(u'\xff\xfe\x00\x00c\x00\x00\x00a\x00\x00\x00f\x00\x00\x00\xe9\x00\x00\x00', output_encoding='utf-16', input_encoding='utf-32')
        self.assertEqual(res, '\xff\xfec\x00a\x00f\x00\xe9\x00')

        # exceptions
        self.assertRaises(UnicodeDecodeError, encode, 'café', output_encoding='ascii', input_encoding='utf-8')
        self.assertRaises(UnicodeDecodeError, encode, u'café', output_encoding='ascii', input_encoding='utf-8')

        self.assertRaises(UnicodeDecodeError, encode, 'Y2Fmw6k=\n', output_encoding='ascii', input_encoding='base64')
        self.assertRaises(UnicodeDecodeError, encode, u'Y2Fmw6k=\n', output_encoding='ascii', input_encoding='base64')


    # @unittest.skip("test_decode")
    def test_decode(self):

        # apply (utf-8)
        self.assertEqual(type(decode(s1)), unicode)
        self.assertEqual(type(decode(s2)), unicode)
        self.assertEqual(type(decode(u1)), unicode)
        self.assertEqual(type(decode(u2)), unicode)

        self.assertEqual(decode(s1), u1)
        self.assertEqual(decode(s2), u2)
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

        # advanced decoding
        res = decode('café', 'utf-8')
        self.assertEqual(res, u'café')
        res = decode(u'café', 'utf-8')
        self.assertEqual(res, u'café')

        res = decode('\xff\xfec\x00a\x00f\x00\xe9\x00', 'utf-16')
        self.assertEqual(res, u'café')
        res = decode(u'\xff\xfec\x00a\x00f\x00\xe9\x00', 'utf-16')
        self.assertEqual(res, u'café')

        res = decode('\xff\xfe\x00\x00c\x00\x00\x00a\x00\x00\x00f\x00\x00\x00\xe9\x00\x00\x00', 'utf-32')
        self.assertEqual(res, u'café')
        res = decode(u'\xff\xfe\x00\x00c\x00\x00\x00a\x00\x00\x00f\x00\x00\x00\xe9\x00\x00\x00', 'utf-32')
        self.assertEqual(res, u'café')

        res = decode('Y2Fmw6k=\n', 'base64')
        self.assertEqual(res, u'café')
        res = decode(u'Y2Fmw6k=\n', 'base64')
        self.assertEqual(res, u'café')

        res = decode('caf\xe9', 'latin-1')
        self.assertEqual(res, u'café')
        res = decode(u'caf\xe9', 'latin-1')
        self.assertEqual(res, u'café')

        res = decode('//5jAGEAZgDpAA==\n', 'base64', detect='utf-16')
        self.assertEqual(res, u'café')
        res = decode(u'//5jAGEAZgDpAA==\n', 'base64', detect='utf-16')
        self.assertEqual(res, u'café')

        res = decode('//4AAGMAAABhAAAAZgAAAOkAAAA=\n', 'base64', detect='utf-32')
        self.assertEqual(res, u'café')
        res = decode(u'//4AAGMAAABhAAAAZgAAAOkAAAA=\n', 'base64', detect='utf-32')
        self.assertEqual(res, u'café')

        # auto detect inner encoding
        res = decode('//5jAGEAZgDpAA==\n', 'base64')
        self.assertEqual(res, u'café')
        res = decode(u'//5jAGEAZgDpAA==\n', 'base64')
        self.assertEqual(res, u'café')

        res = decode('//4AAGMAAABhAAAAZgAAAOkAAAA=\n', 'base64')
        self.assertEqual(res, u'café')
        res = decode(u'//4AAGMAAABhAAAAZgAAAOkAAAA=\n', 'base64')
        self.assertEqual(res, u'café')


    # @unittest.skip("test_encoding_composition")
    def test_encoding_composition(self):

        self.assertEqual(decode(encode('café')), u'café')
        self.assertEqual(decode(encode(u'café')), u'café')

        self.assertEqual(decode(encode('café', 'base64'), 'base64'), u'café')
        self.assertEqual(decode(encode(u'café', 'base64'), 'base64'), u'café')

        self.assertEqual(decode(encode('café', 'latin-1'), 'latin-1'), u'café')
        self.assertEqual(decode(encode(u'café', 'latin-1'), 'latin-1'), u'café')

        self.assertEqual(decode(encode(u'Y2Fmw6k=', 'utf-16', input_encoding='base64'), 'utf-16'), u'café')
        self.assertEqual(decode(encode(u'café', 'utf-16'), 'utf-16'), u'café')

        self.assertEqual(decode(encode('café', 'utf-32'), 'utf-32'), u'café')
        self.assertEqual(decode(encode(u'café', 'utf-32'), 'utf-32'), u'café')


if __name__ == '__main__':
    unittest.main()
