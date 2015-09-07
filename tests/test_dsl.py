#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import unittest

from tocoli import PY2


class TestDSLs(unittest.TestCase):

    # @unittest.skip("skip this test")
    def test_class_Filter(self):
        from tocoli.dsl import Filter

        # string
        res = Filter.string('hello', lambda x: x == 'l')
        self.assertEqual(res, 'll')

        res = Filter.string(u'hello', lambda x: x == 'l')
        self.assertEqual(res, u'll')


        # bytes
        res = Filter.bytes('hello', lambda x: x == 'l')
        if PY2:
            self.assertEqual(res, 'll')
        else:
            self.assertEqual(res, b'll')

        res = Filter.bytes(u'hello', lambda x: x == 'l')
        if PY2:
            self.assertEqual(res, 'll')
        else:
            self.assertEqual(res, b'll')


        # list
        res = Filter.list([1, 2], lambda x: x == 1)
        self.assertEqual(res, [1])


        # iter
        res = Filter.iter(iter([1, 2]), lambda x: x == 1)
        self.assertEqual(res, [1])


        # tuple
        res = Filter.tuple((1, 2), lambda x: x == 1)
        self.assertEqual(res, [1])


        # set
        res = Filter.set({1, 2}, lambda x: x == 1)
        self.assertEqual(res, {1})


        # dict
        res = Filter.Dict.by.key({1: 'one', 2: 'two'}, [1])
        self.assertEqual(res, {1: 'one', 2: 'two'})

        res = Filter.Dict.by.key({1: 'one', 2: 'two'}, [3])
        self.assertEqual(res, None)

        res = Filter.Dict.by.value({1: 'one', 2: 'two'}, ['one'])
        self.assertEqual(res, {1: 'one', 2: 'two'})

        res = Filter.Dict.by.value({1: 'one', 2: 'two'}, ['three'])
        self.assertEqual(res, None)

        # Strings

        res = Filter.Strings.by.similarity(['one', 'two', 'three'], ['wo'], ratio=0.5)
        self.assertEqual(res, ['two'])

        res = Filter.Strings.by.similarity(['one', 'two', 'three'], ['four'])
        self.assertEqual(res, [])

        res = Filter.Strings.by.keywords(['one', 'two', 'three'], ['two'])
        self.assertEqual(res, ['two'])

        res = Filter.Strings.by.keywords(['one', 'two', 'three'], ['four'])
        self.assertEqual(res, [])

        # Dicts
        res = Filter.Dicts.by.key([{1: 'one', 2: 'two'} , {3: 'three'}], [1])
        self.assertEqual(res, [{1: 'one', 2: 'two'}])

        res = Filter.Dicts.by.key([{1: 'one', 2: 'two'} , {3: 'three'}], [3])
        self.assertEqual(res, [{3: 'three'}])

        res = Filter.Dicts.by.key([{1: 'one', 2: 'two'} , {3: 'three'}], [4])
        self.assertEqual(res, [])

        res = Filter.Dicts.by.value([{1: 'one', 2: 'two'} , {3: 'three'}], ['two'])
        self.assertEqual(res, [{1: 'one', 2: 'two'}])

        res = Filter.Dicts.by.value([{1: 'one', 2: 'two'} , {3: 'three'}], ['three'])
        self.assertEqual(res, [{3: 'three'}])

        res = Filter.Dicts.by.value([{1: 'one', 2: 'two'} , {3: 'three'}], ['four'])
        self.assertEqual(res, [])


    # @unittest.skip("skip this test")
    def test_class_Sort(self):
        from tocoli.dsl import Sort

        # string
        res = Sort.string('hello')
        self.assertEqual(res, 'ehllo')

        res = Sort.string(u'hellö')
        self.assertEqual(res, u'ehllö')

        # bytes
        res = Sort.bytes('hello')
        if PY2:
            self.assertEqual(res, 'ehllo')
        else:
            self.assertEqual(res, b'ehllo')

        res = Sort.bytes(u'hello')
        if PY2:
            self.assertEqual(res, 'ehllo')
        else:
            self.assertEqual(res, b'ehllo')

        # list
        res = Sort.list(['b', 'a', 'c'])
        self.assertEqual(res, ['a', 'b', 'c'])

        # iter
        res = Sort.iter(iter(['b', 'a', 'c']))
        self.assertEqual(res, ['a', 'b', 'c'])

        # tuple
        res = Sort.tuple((1, 3, 2))
        self.assertEqual(res, [1, 2, 3])

        # set
        res = Sort.set(set([1, 3, 2, 3, 2]))
        self.assertEqual(res, [1, 2, 3])

        # dict
        res = Sort.Dict.by.key({2: 'a', 1:'c', 3: 'b'})
        self.assertEqual(res, [(1, 'c'), (2, 'a'), (3, 'b')])

        res = Sort.Dict.by.key({2: 'a', 1:'c', 3: 'b'}, reverse=True)
        self.assertEqual(res, [(3, 'b'), (2, 'a'), (1, 'c')])

        res = Sort.Dict.by.value({3: 'a', 4: 'c', 1: 'b', 2: 'd'})
        self.assertEqual(res, [(3, 'a'), (1, 'b'), (4, 'c'), (2, 'd')])

        res = Sort.Dict.by.value({3: 'a', 4: 'c', 1: 'b', 2: 'd'}, reverse=True)
        self.assertEqual(res, [(2, 'd'), (4, 'c'), (1, 'b'), (3, 'a')])

        # Strings
        l = ['schnello', 'bello', 'ello', 'Hello', 'hello', 'trello']

        res = Sort.Strings.by.similarity(l, 'hello')
        self.assertEqual(res, ['trello', 'schnello', 'bello', 'ello', 'Hello', 'hello'])

        res = Sort.Strings.by.similarity(l, 'hello', reverse=True)
        self.assertEqual(res, ['Hello', 'hello', 'ello', 'bello', 'schnello', 'trello'])

        res = Sort.Strings.by.similarity(l, 'hello', reverse=True, weights=(1,0))
        self.assertEqual(res, ['Hello', 'hello', 'bello', 'ello', 'schnello', 'trello'])


        # Dicts

        # Simple sort by a key
        dicts = [{'name': 'Eve'},
                 {'name': 'Alice', 'email': 'alice@example.com'},
                 {'email': 'bob@example.com', 'name': 'Bob'}]

        res = Sort.Dicts.by.value(dicts, ['name'])
        self.assertEqual(res,
                         [{'name': 'Alice', 'email': 'alice@example.com'},
                          {'email': 'bob@example.com', 'name': 'Bob'},
                          {'name': 'Eve'}])


        # Advanced sort for multiple keys with custom sort value:

        dicts = [{'price': 100},
                 {'price': 50, 'shipping': 40},
                 {'shipping': 5, 'price': 55}]

        def total(price, shipping):
            return price + shipping

        res = Sort.Dicts.by.value(dicts,
                         ['price', 'shipping'],
                         values=total,
                         default=0)

        self.assertEqual(res, [{'price': 55, 'shipping': 5},
                               {'price': 50, 'shipping': 40},
                               {'price': 100}])


        # Sort dictionaries with non string keys:

        dicts = [{1: False},
                 {2: True, 1: False},
                 {1: True, 2: True}]

        def both(left, right):
            return left and right

        res = Sort.Dicts.by.value(dicts,
                         {1: 'left', 2: 'right'},
                         values=both,
                         default=False,
                         reverse=True)



        self.assertEqual(res, [{1: True, 2: True},
                               {1: False},
                               {1: False, 2: True}])

        # Dicts similarity
        dicts = [{'word': 'schnello'},
                 {'word': 'bello'},
                 {'word': 'ello'},
                 {'word': 'Hello'},
                 {'word': 'hello'},
                 {'word': 'trello'}]

        res = Sort.Dicts.by.similarity(dicts, 'hello', ['word'])
        self.assertEqual(res, [{'word': 'trello'},
                               {'word': 'schnello'},
                               {'word': 'bello'},
                               {'word': 'ello'},
                               {'word': 'Hello'},
                               {'word': 'hello'}])

        res = Sort.Dicts.by.similarity(dicts, 'hello', ['word'], reverse=True)
        self.assertEqual(res, [{'word': 'Hello'},
                               {'word': 'hello'},
                               {'word': 'ello'},
                               {'word': 'bello'},
                               {'word': 'schnello'},
                               {'word': 'trello'}])

    def test_class_Map(self):
        from tocoli.dsl import Map

        def upper(s):
            return s.upper()

        # mixed
        l = [{1: 'one', 2: 'two', 3: 'three'}, {4: 'four', 5: 'five', 6: 'six'}]
        res = Map.any(l, upper)
        self.assertEqual(res, [{1: 'ONE', 2: 'TWO', 3: 'THREE'}, {4: 'FOUR', 5: 'FIVE', 6: 'SIX'}])

        d = {1: ['a', 'b', 'c'], 2: ['a', 'b', 'c'], 3: ['a', 'b', 'c']}
        res = Map.any(d, upper)
        self.assertEqual(res, {1: ['A', 'B', 'C'], 2: ['A', 'B', 'C'], 3: ['A', 'B', 'C']})


    def test_class_Join(self):
        from tocoli.dsl import Join

        res = Join.Strings.by.keywords('Hello World'.split(), ['do not join anything'])
        self.assertEqual(res, ['Hello', 'World'])

        res = Join.Strings.by.keywords('Hello and World'.split(), keywords=['and'])
        self.assertEqual(res, ['Hello World'])

        res = Join.Strings.by.keywords('Hello AND World'.split(), keywords=['and'])
        self.assertEqual(res, ['Hello World'])

        res = Join.Strings.by.keywords('Hello  +  World'.split(), keywords=['+', '-'])
        self.assertEqual(res, ['Hello World'])

        res = Join.Strings.by.keywords('Hello  -  World'.split(), keywords=['+', '-'])
        self.assertEqual(res, ['Hello World'])

        res = Join.Strings.by.keywords(' - Hello + World'.split(), keywords=['+', '-'])
        self.assertEqual(res, ['Hello World'])

        res = Join.Strings.by.keywords('Hello + World - '.split(), keywords=['+', '-'])
        self.assertEqual(res, ['Hello World'])

        res = Join.Strings.by.keywords(' - Hello + World - '.split(), keywords=['+', '-'])
        self.assertEqual(res, ['Hello World'])

        res = Join.Strings.by.keywords('one + two + three + four'.split(), keywords=['+', '-'])
        self.assertEqual(res, ['one two three four'])

        res = Join.Strings.by.keywords('áíó äöü'.split(), ['do not join anything'])
        self.assertEqual(res, ['áíó', 'äöü'])

        res = Join.Strings.by.keywords('áíó and äöü'.split(), keywords=['and'])
        self.assertEqual(res, ['áíó äöü'])



if __name__ == '__main__':
    unittest.main()
