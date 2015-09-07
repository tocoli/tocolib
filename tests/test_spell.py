#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import unittest

from tocoli.spell import *

class TestSpelling(unittest.TestCase):

    def test_lookup(self):


        #
        # STRICT
        #
        res = lookup(u'', Dictionary.latin[STRICT])
        self.assertEqual(res, [])

        res = lookup(u'-', Dictionary.latin[STRICT])
        self.assertEqual(res, [u'-'])

        res = lookup(u'a', Dictionary.latin[STRICT])
        self.assertEqual(res, [u'a|á|ä'])

        res = lookup(u'ä', Dictionary.latin[STRICT])
        self.assertEqual(res, [u'a|á|ä'])

        res = lookup(u'ab', Dictionary.latin[STRICT])
        self.assertEqual(res, [u'a|á|ä', u'b|v'])

        #
        # WIDE
        #
        res = lookup(u'a', Dictionary.latin[WIDE])
        self.assertEqual(res, [u'a|á|ä|o|ó|e'])

        res = lookup(u'ab', Dictionary.latin[WIDE])
        self.assertEqual(res, [u'a|á|ä|o|ó|e', u'b|v|w'])

if __name__ == '__main__':
    unittest.main()
