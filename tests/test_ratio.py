#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from tocoli.ratio import *
from tocoli import ratio

hello = u'Hello'
world = u'World'

class TestRatios(unittest.TestCase):


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
    def test_equal(self):

        res = equal(hello, world)
        self.assertEqual(res, 2/float(5))

        res = equal(world, hello)
        self.assertEqual(res, 2/float(5))

    # @unittest.skip("skip this test")
    def test_meta(self):

        # one function
        res = meta(hello, world, [equal], [1])
        self.assertEqual(res, 0.4)

        res = meta(world, hello, [equal], [1])
        self.assertEqual(res, 0.4)

        res = meta(hello, world, [equal], [0.5])
        self.assertEqual(res, 0.4)

        res = meta(world, hello, [equal], [0.5])
        self.assertEqual(res, 0.4)

        # two functions (same)
        res = meta(hello, world, [equal, equal], [1, 1])
        self.assertEqual(res, 0.4)

        res = meta(world, hello, [equal, equal], [1, 1])
        self.assertEqual(res, 0.4)

        res = meta(hello, world, [equal, equal], [0.5, 1])
        self.assertEqual(res, 0.4000000000000001)

        res = meta(world, hello, [equal, equal], [0.5, 1])
        self.assertEqual(res, 0.4000000000000001)

        res = meta(hello, world, [equal, equal], [1, 2])
        self.assertEqual(res, 0.4000000000000001)

        res = meta(world, hello, [equal, equal], [1, 2])
        self.assertEqual(res, 0.4000000000000001)

        # two functions (different)
        res = meta(hello, world, [equal, levenshtein], [1, 1])
        self.assertEqual(res, 0.30000000000000004)

        res = meta(world, hello, [equal, levenshtein], [1, 1])
        self.assertEqual(res, 0.30000000000000004)

        res = meta(hello, world, [equal, levenshtein], [0.5, 1])
        self.assertEqual(res, 0.26666666666666666)

        res = meta(world, hello, [equal, levenshtein], [0.5, 1])
        self.assertEqual(res, 0.26666666666666666)

        res = meta(hello, world, [equal, levenshtein], [1, 2])
        self.assertEqual(res, 0.26666666666666666)

        res = meta(world, hello, [equal, levenshtein], [1, 2])
        self.assertEqual(res, 0.26666666666666666)


    # @unittest.skip("skip this test")
    def test_similarity(self):
        res = similarity(hello, world)
        self.assertEqual(res, 0.30000000000000004)

        res = similarity(world, hello)
        self.assertEqual(res, 0.30000000000000004)

        res = similarity(hello, u'ello')
        self.assertEqual(res, 0.7444444444444445)

        res = similarity(hello, u'bello')
        self.assertEqual(res, 0.7)

        res = similarity(hello, u'trello')
        self.assertEqual(res, 0.6136363636363636)

        res = similarity(hello, u'resello')
        self.assertEqual(res, 0.5476190476190476)

        res = similarity(hello, u'schnello')
        self.assertEqual(res, 0.4951923076923077)

        # weights (equal, levenshtein)
        res = similarity(hello, u'ello', (1,4))
        self.assertEqual(res, 0.831111111111111)

        res = similarity(hello, u'bello', (1,4))
        self.assertEqual(res, 0.76)

        res = similarity(hello, u'trello', (1,4))
        self.assertEqual(res, 0.6818181818181819)

        res = similarity(hello, u'resello', (1,4))
        self.assertEqual(res, 0.619047619047619)

        res = similarity(hello, u'schnello', (1,4))
        self.assertEqual(res, 0.5673076923076923)


    # @unittest.skip("skip this test")
    def test_median(self):
        from tocoli.ratio import median

        res = median([1, 3, 5])
        self.assertEqual(res, 3.0)

        res = median([1, 3, 5, 7])
        self.assertEqual(res, 4.0)

        res = median([7, 12, 3, 1, 6, 9])
        self.assertEqual(res, 6.5)


if __name__ == '__main__':
    unittest.main()
