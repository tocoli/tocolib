#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import unittest

from tocoli.regex import *

class TestRegex(unittest.TestCase):

    # @unittest.skip("skip this test")
    def test_generate(self):

        self.assertRaises(TypeError, generate, None)

        #
        # 0 char
        #

        res = generate('')
        self.assertEqual(res, '')

        #
        # 1 char
        #

        res = generate('a')
        self.assertEqual(res, 'a')

        res = generate('a', start=True)
        self.assertEqual(res, '^a')

        res = generate('a', end=True)
        self.assertEqual(res, 'a$')

        res = generate('a', match=match.WIDE)
        self.assertEqual(res, 'a.{0,}?')

        res = generate('a', setLike=True)
        self.assertEqual(res, 'a')

        res = generate('a', start=True, match=match.WIDE)
        self.assertEqual(res, '^a.{0,}?')

        res = generate('a', end=True, match=match.WIDE)
        self.assertEqual(res, 'a.{0,}?$')

        res = generate('a', match=match.WIDE, setLike=True)
        self.assertEqual(res, 'a.{0,}?')

        res = generate('a', start=True, match=match.WIDE, setLike=True)
        self.assertEqual(res, '^a.{0,}?')

        res = generate('a', end=True, match=match.WIDE, setLike=True)
        self.assertEqual(res, 'a.{0,}?$')

        res = generate('a', start=True, end=True, match=match.WIDE, setLike=True)
        self.assertEqual(res, '^a.{0,}?$')

        #
        # 2 chars
        #

        res = generate('ab', start=True)
        self.assertEqual(res, '^ab')

        res = generate('ab', end=True)
        self.assertEqual(res, 'ab$')

        res = generate('ab', match=match.WIDE)
        self.assertEqual(res, 'a.{0,}?b.{0,}?')

        res = generate('ab', setLike=True)
        self.assertEqual(res, '(a|b)(a|b)')

        res = generate('ab', start=True, match=match.WIDE)
        self.assertEqual(res, '^a.{0,}?b.{0,}?')

        res = generate('ab', end=True, match=match.WIDE)
        self.assertEqual(res, 'a.{0,}?b$')

        res = generate('ab', match=match.WIDE, setLike=True)
        self.assertEqual(res, '(a|b).{0,}?(a|b).{0,}?')

        res = generate('ab', start=True, match=match.WIDE, setLike=True)
        self.assertEqual(res, '^a.{0,}?b.{0,}?')

        res = generate('ab', end=True, match=match.WIDE, setLike=True)
        self.assertEqual(res, 'a.{0,}?b$')

        res = generate('ab', start=True, end=True, match=match.WIDE, setLike=True)
        self.assertEqual(res, '^a.{0,}?b$')

        #
        # 3 chars
        #

        res = generate('abc', start=True)
        self.assertEqual(res, '^abc')

        res = generate('abc', end=True)
        self.assertEqual(res, 'abc$')

        res = generate('abc', match=match.WIDE)
        self.assertEqual(res, 'a.{0,}?b.{0,}?c.{0,}?')

        res = generate('abc', setLike=True)
        self.assertEqual(res, '(a|b|c)(a|b|c)(a|b|c)')

        res = generate('abc', start=True, match=match.WIDE)
        self.assertEqual(res, '^a.{0,}?b.{0,}?c.{0,}?')

        res = generate('abc', end=True, match=match.WIDE)
        self.assertEqual(res, 'a.{0,}?b.{0,}?c$')

        res = generate('abc', match=match.WIDE, setLike=True)
        self.assertEqual(res, '(a|b|c).{0,}?(a|b|c).{0,}?(a|b|c).{0,}?')

        res = generate('abc', start=True, match=match.WIDE, setLike=True)
        self.assertEqual(res, '^a.{0,}?(b|c).{0,}?(b|c).{0,}?')

        res = generate('abc', end=True, match=match.WIDE, setLike=True)
        self.assertEqual(res, '(a|b).{0,}?(a|b).{0,}?c$')

        res = generate('abc', start=True, end=True, match=match.WIDE, setLike=True)
        self.assertEqual(res, '^a.{0,}?b.{0,}?c$')

        #
        # 4 chars
        #

        res = generate('abcd', start=True)
        self.assertEqual(res, '^abcd')

        res = generate('abcd', end=True)
        self.assertEqual(res, 'abcd$')

        res = generate('abcd', match=match.WIDE)
        self.assertEqual(res, 'a.{0,}?b.{0,}?c.{0,}?d.{0,}?')

        res = generate('abcd', setLike=True)
        self.assertEqual(res, '(a|b|c|d)(a|b|c|d)(a|b|c|d)(a|b|c|d)')

        res = generate('abcd', start=True, match=match.WIDE)
        self.assertEqual(res, '^a.{0,}?b.{0,}?c.{0,}?d.{0,}?')

        res = generate('abcd', end=True, match=match.WIDE)
        self.assertEqual(res, 'a.{0,}?b.{0,}?c.{0,}?d$')

        res = generate('abcd', match=match.WIDE, setLike=True)
        self.assertEqual(res, '(a|b|c|d).{0,}?(a|b|c|d).{0,}?(a|b|c|d).{0,}?(a|b|c|d).{0,}?')

        res = generate('abcd', match=match.WORD_BOUNDARY, setLike=True)
        self.assertEqual(res, '(a|b|c|d)\S{0,}?(a|b|c|d)\S{0,}?(a|b|c|d)\S{0,}?(a|b|c|d)\S{0,}?')

        res = generate('abcd', start=True, match=match.WIDE, setLike=True)
        self.assertEqual(res, '^a.{0,}?(b|c|d).{0,}?(b|c|d).{0,}?(b|c|d).{0,}?')

        res = generate('abcd', end=True, match=match.WIDE, setLike=True)
        self.assertEqual(res, '(a|b|c).{0,}?(a|b|c).{0,}?(a|b|c).{0,}?d$')

        res = generate('abcd', start=True, end=True, match=match.WIDE, setLike=True)
        self.assertEqual(res, '^a.{0,}?(b|c).{0,}?(b|c).{0,}?d$')

if __name__ == '__main__':
    unittest.main()
