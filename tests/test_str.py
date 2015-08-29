#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import unittest

import sample


class TestSimple(unittest.TestCase):

    def test_failure(self):
        self.assertTrue(False)
