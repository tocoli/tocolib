#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tocoli.sort import ASCENDING
from tocoli.sort import DESCENDING

from tocoli.sort import sort_bytes as bytes
from tocoli.sort import sort_string as string
from tocoli.sort import sort_iter as iter
from tocoli.sort import sort_list as list
from tocoli.sort import sort_tuple as tuple
from tocoli.sort import sort_set as set


class dict:
    class by:
        from tocoli.sort import sort_dict_by_key as key
        key = staticmethod(key)

        from tocoli.sort import sort_dict_by_value as value
        value = staticmethod(value)

class strings:
    class by:
        from tocoli.sort import sort_strings_by_similarity as similarity
        similarity = staticmethod(similarity)

class dicts:
    class by:
        from tocoli.sort import sort_dicts_by_value as value
        value = staticmethod(value)

        from tocoli.sort import sort_dicts_by_similarity as similarity
        similarity = staticmethod(similarity)
