#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

from tocoli.type import to_string
from tocoli.map import recursive_map

def join_strings_by_keywords(list, keywords, join=' '):
    """Join strings by keywords. Returns a new list with joined strings."""
    res = []
    append = False
    for i, elem in enumerate(list):
        if (append):
            try:
                res[-1] = res[-1] + join + elem
            except:
                res.append(elem)
            append = False
            continue
        else:
            if any(elem.lower() in s.lower() for s in keywords):
                if (i > 0 and i < len(list)-1):
                    append = True
                else:
                    if(i == 0):
                        append = True
                    else:
                        if (i < len(list)-1):
                            append = True
            else:
                res.append(elem)

    return res


def join_values_as_string(*args, **kwargs):
    """Concatenates all values as one string. Returns a string."""
    return u''.join(recursive_map(
        args + tuple(kwargs[k] for k in sorted(kwargs)), to_string))
