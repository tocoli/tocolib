#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from tocoli import PY2

from tocoli import iteritems

class Tests(unittest.TestCase):

    # @unittest.skip("skip this test")
    def test_recursive_map(self):
        from tocoli.map import recursive_map, DICT

        def add_five(a, _):
            return a + 5

        def decode(b, _, encoding='utf-8'):
            from codecs import decode
            return decode(b, encoding)

        def upper(s, _):
            return s.upper()

        # default
        self.assertEqual(recursive_map(1), 1)
        self.assertEqual(recursive_map(1.0), 1.0)
        self.assertEqual(recursive_map(complex(0,4)), complex(0,4))
        if PY2:
            self.assertEqual(recursive_map('hello'), 'hello')
        else:
            self.assertEqual(recursive_map(bytes('hello', 'utf-8')), b'hello')


        # integers
        res = recursive_map(5, add_five)
        self.assertEqual(res, 10)


        # bytes
        if PY2:
            b = 'café'
        else:
            b = 'café'.encode('utf-8')

        res = recursive_map(b, decode)
        self.assertEqual(res, u'café')

        # string
        s = u'café'
        res = recursive_map(s, upper)
        self.assertEqual(res, u'CAFÉ')

        # list
        l = [1, 2, 3]
        res = recursive_map(l, add_five)
        self.assertEqual(res, [6, 7, 8])

        l = ['a', 'b', u'c']
        res = recursive_map(l, upper)
        self.assertEqual(res, ['A', 'B', u'C'])

        # tuple
        t = (1, 2, 3)
        res = recursive_map(t, add_five)
        self.assertEqual(res, (6, 7, 8))

        t = ('a', 'b', u'c')
        res = recursive_map(t, upper)
        self.assertEqual(res, ('A', 'B', u'C'))

        # set
        s = {1, 2, 3}
        res = recursive_map(s, add_five)
        self.assertEqual(res, {6, 7, 8})

        s = {'a', 'b', u'c'}
        res = recursive_map(s, upper)
        self.assertEqual(res, {'A', 'B', u'C'})

        # dict
        d = {1: 'one', 2: 'two', 3: 'three'}
        res = recursive_map(d, upper)
        self.assertEqual(res, {1: 'ONE', 2: 'TWO', 3: 'THREE'})

        # mixed
        l = [{1: 'one', 2: 'two', 3: 'three'}, {4: 'four', 5: 'five', 6: 'six'}]
        res = recursive_map(l, upper)
        self.assertEqual(res, [{1: 'ONE', 2: 'TWO', 3: 'THREE'}, {4: 'FOUR', 5: 'FIVE', 6: 'SIX'}])

        d = {1: ['a', 'b', 'c'], 2: ['a', 'b', 'c'], 3: ['a', 'b', 'c']}
        res = recursive_map(d, upper)
        self.assertEqual(res, {1: ['A', 'B', 'C'], 2: ['A', 'B', 'C'], 3: ['A', 'B', 'C']})


        def upper_dict_values(item, _):
            for k, v in iteritems(d):
                if hasattr(v, '__iter__'):
                    d[k] = [elem.upper() for elem in v]
                else:
                    d[k] = elem.upper()
            return d

        res = recursive_map(d, upper_dict_values, DICT)
        self.assertEqual(res, {1: ['A', 'B', 'C'], 2: ['A', 'B', 'C'], 3: ['A', 'B', 'C']})


    # @unittest.skip("skip this test")
    def test_map_to_non_accented_characters(self):
        from tocoli.map import map_to_non_accented_characters

        res = map_to_non_accented_characters(u'áíóäöü')
        self.assertEqual(res, u'aioaou')


if __name__ == '__main__':
    unittest.main()
