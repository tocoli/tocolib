#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

from tocoli import binary_type, text_type, integer_types,iteritems
from tocoli.fn import identity


MAP_NONE = 0
MAP_NUMERIC = 1
MAP_STR = 2
MAP_LIST = 4
MAP_TUPLE = 8
MAP_SET = 16
MAP_DICT_KEY = 32
MAP_DICT_VALUE = 64
MAP_DICT = MAP_DICT_KEY | MAP_DICT_VALUE
MAP_OTHER = 128
MAP_ALL = 255
MAP_DEFAULT = MAP_ALL ^ MAP_DICT_KEY


def map(item, function=identity, flags=MAP_DEFAULT):
    """ Maps any function recursivly to the item. """

    res = item

    if isinstance(item, binary_type):
        if (flags & MAP_STR):
            res = function(item)
    elif isinstance(item, text_type):
        if (flags & MAP_STR):
            res = function(item)
    elif isinstance(item, list):
        if (flags & MAP_LIST):
            res = list(map(elem, function, flags) for elem in item)
    elif isinstance(item, tuple):
        if (flags & MAP_TUPLE):
            res = tuple(map(elem, function, flags) for elem in item)
    elif isinstance(item, set):
        if (flags & MAP_SET):
            res = set(map(elem, function, flags) for elem in item)
    elif isinstance(item, dict):
        res = {}
        for key, value in iteritems(item):
            if (flags & MAP_DICT_KEY):
                k = map(key, function, flags)
            else:
                k = key

            if (flags & MAP_DICT_VALUE):
                v = map(value, function, flags)
            else:
                v = value

            res[k] = v
    elif isinstance(item, integer_types) or isinstance(item, float) or isinstance(item, complex):
        if (flags & MAP_NUMERIC):
            res = function(item)
    else:
        if (flags & MAP_OTHER):
            try:
                res = function(item)
            except:
                raise TypeError("Not implementet for " + str(type(item)))

    return res
