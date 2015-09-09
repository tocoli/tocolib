#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import unicodedata
from tocoli import binary_type, text_type, integer_types,iteritems
from tocoli.fn import first_arg


NONE = 0
STRING = 1
BYTES = 2
NUMERIC = 4
LIST = 8
LIST_VALUE = 16
TUPLE = 32
TUPLE_VALUE = 64
SET = 128
SET_VALUE = 256
DICT = 512
DICT_KEY = 1024
DICT_VALUE = 2048
OTHER = 4096
ALL = 8191
DEFAULT = ALL ^ LIST ^ TUPLE ^ SET ^ DICT ^ DICT_KEY


def recursive_map(item, function=first_arg, flags=DEFAULT, parent=None):
    """ Maps any function recursivly to the item. """

    r = item

    if isinstance(item, text_type):
        if (flags & STRING):
            r = function(item, parent)
    elif isinstance(item, binary_type):
        if (flags & BYTES):
            r = function(item, parent)
    elif isinstance(item, integer_types) or isinstance(item, float) or isinstance(item, complex):
        if (flags & NUMERIC):
            r = function(item, parent)
    elif isinstance(item, list):
        if (flags & LIST):
            r = function(item, parent)
        else:
            if (flags & LIST_VALUE):
                r = list(recursive_map(elem, function, flags, item) for elem in item)
    elif isinstance(item, tuple):
        if (flags & TUPLE):
            r = function(item, parent)
        else:
            if (flags & TUPLE_VALUE):
                r = tuple(recursive_map(elem, function, flags, item) for elem in item)
    elif isinstance(item, set):
        if (flags & SET):
            r = function(item, parent)
        else:
            if (flags & SET_VALUE):
                r = set(recursive_map(elem, function, flags, item) for elem in item)
    elif isinstance(item, dict):
        if (flags & DICT):
            r = function(item, parent)
        else:
            r = {}
            for key, value in iteritems(item):
                if (flags & DICT_KEY):
                    k = recursive_map(key, function, flags, item)
                else:
                    k = key

                if (flags & DICT_VALUE):
                    v = recursive_map(value, function, flags, item)
                else:
                    v = value

                r[k] = v
    else:
        if (flags & OTHER):
            r = function(item, parent)

    return r


def map_to_non_accented_characters(str):
    """Returns a non accented string."""
    return u''.join(c for c in unicodedata.normalize('NFD', str)
                        if unicodedata.category(c) != 'Mn')
