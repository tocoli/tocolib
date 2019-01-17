#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestTest(unittest.TestCase):

    # @unittest.skip("skip this test")
    def test_bench(self):
        from tocoli.test import bench, Bencher

        # Test 1 - add()
        def add(a, b):
            return a + b

        res = bench(add, 2, 3)
        self.assertEqual(res, 5)

        b = Bencher(rounds=2)
        res = b.bench(add, 1 + 1, 3)
        self.assertEqual(res, 5)

        b = Bencher(rounds=3, collect=True)
        res = b.bench(add, 1 + 1, 3)
        self.assertEqual(res, [5, 5, 5])

        b = Bencher(stopwatch=False)
        res = b.bench(add, 2, 3)
        self.assertEqual(res, 5)

        # Test 2 - echo()
        def echo(a):
            return a

        res = bench(echo, 'a')
        self.assertEqual(res, 'a')
        res = bench(echo, 1)
        self.assertEqual(res, 1)
        res = bench(echo, (1, 2))
        self.assertEqual(res, (1, 2))
        res = bench(echo, [1, 2])
        self.assertEqual(res, [1, 2])

        # sleep

        from time import sleep
        b = Bencher(rounds=10, precision='.10')
        res = b.bench(sleep, 0.001)
        self.assertEqual(res, None)

    # @unittest.skip("skip this test")
    def test_fnprint(self):
        from tocoli.test import fnprint

        def concat(a, b, c):
            return str(a) + str(b) + str(c)

        fnprint(concat, a='aaa', b='b', c='c')

        def mult(a, b):
            return a * b

        fnprint(mult, 2, 5)


if __name__ == '__main__':
    unittest.main()
