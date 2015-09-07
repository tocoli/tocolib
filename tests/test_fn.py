#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import unittest
from tocoli.fn import *
from tocoli import fn

# class TestRecursive(unittest.TestCase):

#     # @unittest.skip("skip this test")
#     def test_map(self):

#         self.assertRaises(UnicodeEncodeError, recursive.map, u"üñíḉôdè", lambda s: s.decode('utf-8'))

#         res = recursive.map(None)
#         self.assertEqual(res, None)

#         #
#         # Numeric
#         #

#         res = recursive.map(1)
#         self.assertEqual(res, 1)
#         self.assertEqual(type(res), type(1))

#         res = recursive.map(long(1))
#         self.assertEqual(res, long(1))
#         self.assertTrue(isinstance(res, long))

#         res = recursive.map(1.0)
#         self.assertEqual(res, 1.0)
#         self.assertEqual(type(res), type(1.0))

#         res = recursive.map(1, lambda x: x+1)
#         self.assertEqual(res, 2)
#         self.assertEqual(type(res), type(2))

#         res = recursive.map(2, lambda x: x*x)
#         self.assertEqual(res, 4)
#         self.assertEqual(type(res), type(4))

#         #
#         # String
#         #

#         res = recursive.map("str")
#         self.assertEqual(res, u"str")

#         res = recursive.map("üñíḉôdè_as_str")
#         self.assertEqual(res, u"üñíḉôdè_as_str")

#         res = recursive.map(u"unicode")
#         self.assertEqual(res, u"unicode")

#         res = recursive.map(u"üñíḉôdè")
#         self.assertEqual(res, u"üñíḉôdè")

#         res = recursive.map("üñíḉôdè_as_str")
#         self.assertEqual(res, u"üñíḉôdè_as_str")

#         res = recursive.map(u"üñíḉôdè_as_str")
#         self.assertEqual(res, u"üñíḉôdè_as_str")

#         #
#         # List
#         #

#         # numeric
#         res = recursive.map([1, 2, 3])
#         self.assertEqual(res, [1, 2, 3])

#         res = recursive.map([1, 2, 3], lambda x: x+1)
#         self.assertEqual(res, [2, 3, 4])

#         res = recursive.map([1, 2, 3], lambda x: x*x)
#         self.assertEqual(res, [1, 4, 9])

#         res = recursive.map([1.1, 2.2, 3.3])
#         self.assertEqual(res, [1.1, 2.2, 3.3])

#         res = recursive.map([1.1, 2.2, 3.3], lambda x: x+1.1)
#         self.assertEqual(res, [2.2, 3.3000000000000003, 4.4])

#         res = recursive.map([1, 2, 3], lambda x: x*x)
#         self.assertEqual(res, [1, 4, 9])

#         # str & unicode
#         res = recursive.map(["Hello", "World"])
#         self.assertEqual(res, [u"Hello", u"World"])

#         res = recursive.map(["Hello", "World"])
#         self.assertEqual(res, [u"Hello", u"World"])

#         res = recursive.map(["Hello", u"World"])
#         self.assertEqual(res, [u"Hello", u"World"])

#         res = recursive.map(["Hello", "Wörld"])
#         self.assertEqual(res, [u"Hello", u"Wörld"])

#         res = recursive.map(["Hello", u"Wörld"])
#         self.assertEqual(res, [u"Hello", u"Wörld"])

#         # list
#         res = recursive.map([[], []])
#         self.assertEqual(res, [[], []])

#         res = recursive.map([['ü'], ['ö']], unicode.upper)
#         self.assertEqual(res, [[u'Ü'], [u'Ö']])

#         # mixed
#         res = recursive.map([{}, {}])
#         self.assertEqual(res, [{}, {}])

#         # print MAP_ALL
#         # print MAP_DEFAULT
#         # print MAP_DEFAULT | MAP_DICT
#         # print MAP_DEFAULT | MAP_DICT_KEY

#         res = recursive.map([{'í': 'ó'}, {'ä': 'ö'}], unicode.upper)
#         self.assertEqual(res, [{u'í': u'Ó'}, {u'ä': u'Ö'}])

#         res = recursive.map([{'í': 'ó'}, {'ä': 'ö'}], unicode.upper, MAP_DEFAULT | MAP_DICT)
#         self.assertEqual(res, [{u'Í': u'Ó'}, {u'Ä': u'Ö'}])

#         res = recursive.map([{'í': 'ó'}, {'ä': 'ö'}, (u"Ä", "b"), ["c"]], unicode.upper, MAP_DEFAULT | MAP_DICT_KEY)
#         self.assertEqual(res, [{u'Í': u'Ó'}, {u'Ä': u'Ö'}, (u"Ä", u"B"), [u"C"]])

#         res = recursive.map(['ä', 2, 'b', 4], unicode.upper, MAP_DEFAULT ^ MAP_NUMERIC)
#         self.assertEqual(res, [u'Ä', 2, u'B', 4])

#         #
#         # Dict
#         #

#         res = recursive.map({"Hello": "World"})
#         self.assertEqual(res, {u"Hello": u"World"})

#         res = recursive.map({"Hello": True, "World": True})
#         self.assertEqual(res, {u"Hello": True, u"World": True})

#         res = recursive.map({"Hellö": True, "Wörld": True})
#         self.assertEqual(res, {u"Hellö": True, u"Wörld": True})

#         res = recursive.map({u"Hellö": True, u"Wörld": True})
#         self.assertEqual(res, {u"Hellö": True, u"Wörld": True})

#         # upper()
#         res = recursive.map({"Hello": "World"}, lambda x: x.upper())
#         self.assertEqual(res, {u"Hello": u"WORLD"})

#         res = recursive.map({"Hello": "World"}, lambda x: x.upper(), MAP_DEFAULT | MAP_DICT_KEY)
#         self.assertEqual(res, {u"HELLO": u"WORLD"})

#         res = recursive.map({"Hello": "World"}, lambda x: x.upper(), MAP_DEFAULT | MAP_DICT)
#         self.assertEqual(res, {u"HELLO": u"WORLD"})

#         res = recursive.map({"Hello": "World"}, unicode.upper)
#         self.assertEqual(res, {u"Hello": u"WORLD"})

#         res = recursive.map({"Hello": "World"}, unicode.upper, MAP_DEFAULT | MAP_DICT_KEY)
#         self.assertEqual(res, {u"HELLO": u"WORLD"})

#         res = recursive.map({"Hello": "World"}, unicode.upper, MAP_DEFAULT | MAP_DICT)
#         self.assertEqual(res, {u"HELLO": u"WORLD"})

#         # lower()
#         res = recursive.map({"Hello": "World"}, lambda x: x.lower())
#         self.assertEqual(res, {u"Hello": u"world"})

#         res = recursive.map({"Hello": "World"}, lambda x: x.lower(), MAP_DEFAULT | MAP_DICT_KEY)
#         self.assertEqual(res, {u"hello": u"world"})

#         res = recursive.map({"Hello": "World"}, unicode.lower)
#         self.assertEqual(res, {u"Hello": u"world"})

#         res = recursive.map({"Hello": "World"}, unicode.lower, MAP_DEFAULT | MAP_DICT_KEY)
#         self.assertEqual(res, {u"hello": u"world"})


# class TestSort(unittest.TestCase):

#     def test_dictionaries(self):
#         from rigs.test import fnprint

#         dicts = [{'key1': 'val1', 'key2': 'val2'},
#                  {'key1': 'val3'},
#                  {'key1': 'val4'},
#                  {'key1': 'val7'},
#                  {'key1': 'val6'},
#                  {'key1': 'val5'},
#                  {'key2': 'val1'},
#                  {'key2': 'val2'},
#                  {'key3': 'val1'},
#                  {'key3': 'val2'}]

#         res = fnprint(Sort.dictionaries, dicts)
#         print len(res)

#         res = fnprint(Sort.dictionaries, dicts, where=lambda key, _: key == 'key1')
#         print len(res)

#         res = fnprint(Sort.dictionaries, dicts, where=lambda _, val: val == 'val1', filterDict=lambda d: 'key1' in d.keys() )
#         print len(res)

#         res = fnprint(Sort.dictionaries, dicts, filterDict=lambda d: 'val1' in d.values() )
#         print len(res)


# class TestSortKey(unittest.TestCase):

#     def test_key(self):

#         self.assertRaises(IndexError, Sort.Key.key, '')

#         res = Sort.Key.key('a')
#         self.assertEqual(res, 'a')

#         res = Sort.Key.key(['key', 'val'])
#         self.assertEqual(res, 'key')

#         res = Sort.Key.key(('key', 'val'))
#         self.assertEqual(res, 'key')

#         self.assertRaises(KeyError, Sort.Key.key, {'key': 'val'})

#         res = Sort.Key.key({'key2': 'val', 'key1': 'val'}, 'val')
#         self.assertEqual(res, ['key1', 'key2'])

#         res = Sort.Key.key({'key2': 'val', 'key1': 'val'}, 'val', True)
#         self.assertEqual(res, ['key2', 'key1'])

#         res = Sort.Key.key({1: 'val', 2: 'val'}, 'val')
#         self.assertEqual(res, [1, 2])

#         res = Sort.Key.key({2: 'val', 1: 'val'}, 'val')
#         self.assertEqual(res, [1, 2])

#         res = Sort.Key.key({1: 'val', 2: 'val'}, 'val', True)
#         self.assertEqual(res, [2, 1])

#         res = Sort.Key.key({2: 'val', 1: 'val'}, 'val', True)
#         self.assertEqual(res, [2, 1])

#         res = Sort.Key.key(dict([['key', 'val']]), 'val')
#         self.assertEqual(res, ['key'])

#         res = Sort.Key.key(dict([('key', 'val')]), 'val')
#         self.assertEqual(res, ['key'])


#         res = sorted([{3: 'val1', 2: 'val2'}, {3: 'val1'}, {3: 'val1', 5: 'val2', 2: 'val3'}, {1: 'val1'}, {2: 'val1'}, {4: None}], lambda a, b: 0)
#         print(res)







# class TestSortBy(unittest.TestCase):
#     #@unittest.skip("skip this test")
#     def test_by_similarity(self):

#         #
#         # non iterable
#         #
#         self.assertRaises(TypeError, Sort.by.similarity, 1)

#         #
#         # iterable
#         #
#         res = Sort.by.similarity('')
#         self.assertEqual(res, [])

#         res = Sort.by.similarity('', '')
#         self.assertEqual(res, [])

#         res = Sort.by.similarity([])
#         self.assertEqual(res, [])

#         res = Sort.by.similarity([], '')
#         self.assertEqual(res, [])

#         res = Sort.by.similarity(())
#         self.assertEqual(res, [])

#         res = Sort.by.similarity((), '')
#         self.assertEqual(res, [])

#         res = Sort.by.similarity({})
#         self.assertEqual(res, [])

#         res = Sort.by.similarity({}, '')
#         self.assertEqual(res, [])

#         # one elem

#         res = Sort.by.similarity('a')
#         self.assertEqual(res, ['a'])

#         res = Sort.by.similarity('ä')
#         self.assertEqual(res, ['\xa4', '\xc3'])

#         res = Sort.by.similarity(u'ä')
#         self.assertEqual(res, [u'ä'])

#         # mixed iterables




#         key = 'a123'

#         unsorted_serials = ['A-321baam',
#                             'A-123',
#                             'A123',
#                             'A-321',
#                             'a123',
#                             'abcdef',
#                             'A231',
#                             '12bcdef',
#                             'A312',
#                             'bcdef',
#                             'A321',
#                             'a12bcdef']

#         sorted_serials = ['A-123',
#                           'A123',
#                           'a123',
#                           'A231',
#                           'A312',
#                           'A-321',
#                           'A321',
#                           'A-321baam',
#                           'a12bcdef',
#                           '12bcdef',
#                           'abcdef',
#                           'bcdef']

#         res = Sort.by.similarity(unsorted_serials, key)
#         self.assertEqual(res, sorted_serials)

#         # print 'sorted serials:'
#         # for r in res:
#         #     print r


# class TestFilter(unittest.TestCase):

#     # @unittest.skip("skip this test")
#     def test_by_ratio(self):

#         good_key = "FA1001"
#         good_list = ['f-100a15',
#                      'f-100a14',
#                      'f-101a70',
#                      'f-10a01',
#                      'f-101a15',
#                      'f-101a90',
#                      'f-100a13',
#                      'f-101a10']

#         bad_key = "FA0351"
#         bad_list = ['f-100a15',
#                     'f-103a43',
#                     'f-101a73',
#                     'f-103a30',
#                     'f-100a14',
#                     'f-100a65',
#                     'f-101a63',
#                     'f-101a70',
#                     'f-102a55',
#                     'f-103a34',
#                     'f-103a59',
#                     'f-105a43',
#                     'f-107a55',
#                     'f-10a01',
#                     'f-15a00',
#                     'f-30a30',
#                     'f-53a50',
#                     'f-101a15',
#                     'f-101a90',
#                     'f-100a13',
#                     'f-101a10']

#         ratio = 0.75
#         good_filtered_list = Filter.by.ratio(good_list, good_key, ratio=ratio)
#         # print 'good_filtered_list ({}, {})'.format(good_key, ratio)
#         # for r in good_filtered_list:
#         #     print(r)

#         bad_filtered_list = Filter.by.ratio(bad_list, bad_key, ratio=ratio)
#         # print 'bad_filtered_list ({}, {})'.format(bad_key, ratio)
#         # for r in bad_filtered_list:
#         #     print(r)

if __name__ == '__main__':
    unittest.main()
