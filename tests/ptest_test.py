#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import unittest
from tocoli.test import *


class TestTest(unittest.TestCase):

    # @unittest.skip("skip this test")
    def test_bench(self):

        # Test 1 - add()
        def add(a, b):
            return a + b

        res = bench(add, (2, 3))
        self.assertEquals(res, 5)

        res = bench(add, (1+1, 3), 2)
        self.assertEquals(res, 5)

        res = bench(add, (1+1, 3), 2, collect=True)
        self.assertEquals(res, [5, 5])

        bench(add, (2, 3), 10000, precision='.6')

        res = bench(add, (2, 3), stopwatch=False)
        self.assertEquals(res, 5)

        # Test 2 - echo()
        def echo(a):
            return a

        res = bench(echo, 'a')
        self.assertEquals(res, 'a')
        res = bench(echo, 1)
        self.assertEquals(res, 1)
        res = bench(echo, (1, 2))
        self.assertEquals(res, (1, 2))
        res = bench(echo, [1, 2])
        self.assertEquals(res, [1, 2])

    # @unittest.skip("skip this test")
    def test_fnprint(self):

        def concat(a, b, c): return str(a) + str(b) + str(c)

        fnprint(concat, a='aaa', b='b', c='c')

        def mult(a, b): return a * b

        fnprint(mult, 2, 5)

if __name__ == '__main__':
    unittest.main()
