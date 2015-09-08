#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

from tocoli import binary_type, text_type, integer_types,iteritems
from tocoli.fn import first_arg


NONE = 0
STR = 1
BYTES = 2
NUMERIC = 4
LIST = 8
TUPLE = 16
SET = 32
DICT_KEY = 64
DICT_VALUE = 128
DICT = 256
OTHER = 512
ALL = 1023
DEFAULT = ALL ^ DICT_KEY ^ DICT


def map(item, function=first_arg, flags=DEFAULT, parent=None):
    """ Maps any function recursivly to the item. """

    r = item

    if isinstance(item, text_type):
        if (flags & STR):
            r = function(item, parent)
    elif isinstance(item, binary_type):
        if (flags & BYTES):
            r = function(item, parent)
    elif isinstance(item, integer_types) or isinstance(item, float) or isinstance(item, complex):
        if (flags & NUMERIC):
            r = function(item, parent)
    elif isinstance(item, list):
        if (flags & LIST):
            r = list(map(elem, function, flags, item) for elem in item)
    elif isinstance(item, tuple):
        if (flags & TUPLE):
            r = tuple(map(elem, function, flags, item) for elem in item)
    elif isinstance(item, set):
        if (flags & SET):
            r = set(map(elem, function, flags, item) for elem in item)
    elif isinstance(item, dict):
        if (flags & DICT):
            r = function(item, parent)
        else:
            r = {}
            for key, value in iteritems(item):
                if (flags & DICT_KEY):
                    k = map(key, function, flags, item)
                else:
                    k = key

                if (flags & DICT_VALUE):
                    v = map(value, function, flags, item)
                else:
                    v = value

                r[k] = v
    else:
        if (flags & OTHER):
            try:
                r = function(item, parent)
            except:
                raise TypeError("Not implementet for " + str(type(item)))

    return r
