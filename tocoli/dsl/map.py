#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tocoli.map import recursive_map as recursive
from tocoli.map import (NONE,
                        STRING,
                        BYTES,
                        NUMERIC,
                        LIST,
                        LIST_VALUE,
                        TUPLE,
                        TUPLE_VALUE,
                        SET,
                        SET_VALUE,
                        DICT,
                        DICT_KEY,
                        DICT_VALUE,
                        OTHER,
                        ALL,
                        DEFAULT)


class string:
    from tocoli.map import map_to_non_accented_characters as non_accented
    non_accented = staticmethod(non_accented)
