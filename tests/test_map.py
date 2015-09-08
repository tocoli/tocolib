#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import unittest
from tocoli import PY2

from tocoli import iteritems

class Tests(unittest.TestCase):

    # @unittest.skip("skip this test")
    def test_map(self):
        from tocoli.map import map, DICT

        def add_five(a, _):
            return a + 5

        def decode(b, _, encoding='utf-8'):
            from codecs import decode
            return decode(b, encoding)

        def upper(s, _):
            return s.upper()

        # default
        self.assertEqual(map(1), 1)
        self.assertEqual(map(1.0), 1.0)
        self.assertEqual(map(complex(0,4)), complex(0,4))
        if PY2:
            self.assertEqual(map('hello'), 'hello')
        else:
            self.assertEqual(map(bytes('hello', 'utf-8')), b'hello')


        # integers
        res = map(5, add_five)
        self.assertEqual(res, 10)


        # bytes
        if PY2:
            b = 'café'
        else:
            b = 'café'.encode('utf-8')

        res = map(b, decode)
        self.assertEqual(res, u'café')

        # string
        s = u'café'
        res = map(s, upper)
        self.assertEqual(res, u'CAFÉ')

        # list
        l = [1, 2, 3]
        res = map(l, add_five)
        self.assertEqual(res, [6, 7, 8])

        l = ['a', 'b', u'c']
        res = map(l, upper)
        self.assertEqual(res, ['A', 'B', u'C'])

        # tuple
        t = (1, 2, 3)
        res = map(t, add_five)
        self.assertEqual(res, (6, 7, 8))

        t = ('a', 'b', u'c')
        res = map(t, upper)
        self.assertEqual(res, ('A', 'B', u'C'))

        # set
        s = {1, 2, 3}
        res = map(s, add_five)
        self.assertEqual(res, {6, 7, 8})

        s = {'a', 'b', u'c'}
        res = map(s, upper)
        self.assertEqual(res, {'A', 'B', u'C'})

        # dict
        d = {1: 'one', 2: 'two', 3: 'three'}
        res = map(d, upper)
        self.assertEqual(res, {1: 'ONE', 2: 'TWO', 3: 'THREE'})

        # mixed
        l = [{1: 'one', 2: 'two', 3: 'three'}, {4: 'four', 5: 'five', 6: 'six'}]
        res = map(l, upper)
        self.assertEqual(res, [{1: 'ONE', 2: 'TWO', 3: 'THREE'}, {4: 'FOUR', 5: 'FIVE', 6: 'SIX'}])

        d = {1: ['a', 'b', 'c'], 2: ['a', 'b', 'c'], 3: ['a', 'b', 'c']}
        res = map(d, upper)
        self.assertEqual(res, {1: ['A', 'B', 'C'], 2: ['A', 'B', 'C'], 3: ['A', 'B', 'C']})


        def upper_dict_values(item, _):
            for k, v in iteritems(d):
                if hasattr(v, '__iter__'):
                    d[k] = [elem.upper() for elem in v]
                else:
                    d[k] = elem.upper()
            return d

        res = map(d, upper_dict_values, DICT)
        self.assertEqual(res, {1: ['A', 'B', 'C'], 2: ['A', 'B', 'C'], 3: ['A', 'B', 'C']})


if __name__ == '__main__':
    unittest.main()
