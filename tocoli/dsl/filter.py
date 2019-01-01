#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tocoli.filter import filter_bytes as bytes
from tocoli.filter import filter_string as string
from tocoli.filter import filter_iter as iter
from tocoli.filter import filter_list as list
from tocoli.filter import filter_tuple as tuple
from tocoli.filter import filter_set as set


class dict:
    class by:
        from tocoli.filter import filter_dict_by_key as key
        key = staticmethod(key)

        from tocoli.filter import filter_dict_by_value as value
        value = staticmethod(value)


class strings:
    class by:
        from tocoli.filter import filter_strings_by_keywords as keywords
        keywords = staticmethod(keywords)

        from tocoli.filter import filter_strings_by_similarity as similarity
        similarity = staticmethod(similarity)


class dicts:
    class by:
        from tocoli.filter import filter_dicts_by_keys as key
        from tocoli.filter import filter_dicts_by_values as value
        key = staticmethod(key)
        value = staticmethod(value)
