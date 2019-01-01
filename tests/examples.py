#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from pprint import pprint


class Tests(unittest.TestCase):

    # @unittest.skip("skip this test")
    def test_DESCRIPTION(self):

        dicts = [{'firstname': 'Bob',   'lastname': 'Abel'},
                         {'firstname': 'Alice', 'lastname': 'Bond'},
                         {'firstname': 'Carol', 'lastname': 'Bond'},
                         {'firstname': 'Bob',   'lastname': 'Bond'},
                         {'firstname': 'Carol', 'lastname': 'Abel'},
                         {'firstname': 'Alice', 'lastname': 'Abel'}]


        from tocoli.dsl import sort
        res = sort.dicts.by.similarity(dicts, 'Karol', ['firstname'])
        self.assertEqual(res, [{'firstname': 'Carol', 'lastname': 'Bond'},
                               {'firstname': 'Carol', 'lastname': 'Abel'},
                               {'firstname': 'Alice', 'lastname': 'Bond'},
                               {'firstname': 'Alice', 'lastname': 'Abel'},
                               {'firstname': 'Bob', 'lastname': 'Abel'},
                               {'firstname': 'Bob', 'lastname': 'Bond'}])

        from tocoli.dsl import map

        def upper(item, parent):
            return item.upper()

        res = map.recursive(dicts, upper)
        self.assertEqual(res, [{'firstname': 'BOB', 'lastname': 'ABEL'},
                               {'firstname': 'ALICE', 'lastname': 'BOND'},
                               {'firstname': 'CAROL', 'lastname': 'BOND'},
                               {'firstname': 'BOB', 'lastname': 'BOND'},
                               {'firstname': 'CAROL', 'lastname': 'ABEL'},
                               {'firstname': 'ALICE', 'lastname': 'ABEL'}])

        map_keys = (map.DEFAULT | map.DICT_KEY) ^ map.DICT_VALUE
        res = map.recursive(dicts, upper, map_keys)
        self.assertEqual(res, [{'FIRSTNAME': 'Bob', 'LASTNAME': 'Abel'},
                               {'FIRSTNAME': 'Alice', 'LASTNAME': 'Bond'},
                               {'FIRSTNAME': 'Carol', 'LASTNAME': 'Bond'},
                               {'FIRSTNAME': 'Bob', 'LASTNAME': 'Bond'},
                               {'FIRSTNAME': 'Carol', 'LASTNAME': 'Abel'},
                               {'FIRSTNAME': 'Alice', 'LASTNAME': 'Abel'}])


if __name__ == '__main__':
    unittest.main()
