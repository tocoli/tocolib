#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

from tocoli import *
from tocoli.type import to_bool, to_integer


def comparable(left, right, case_sensitive=False):
    """Makes values comparable. Returns a tuple of values"""
    if isinstance(left, string_types) and right is None:
        if case_sensitive:
            return (left, None)
        else:
            return (left.lower(), None)
    if left is None and isinstance(right, string_types):
        if case_sensitive:
            return (None, right)
        else:
            return (None, right.lower())
    if isinstance(left, string_types) and isinstance(right, string_types):
        if case_sensitive:
            return (left, right)
        else:
            return (left.lower(), right.lower())
    elif isinstance(left, string_types) and isinstance(right, integer_types):
        return (to_integer(left), to_integer(right))
    elif isinstance(left, integer_types) and isinstance(right, string_types):
        return (to_integer(left), to_integer(right))
    elif isinstance(left, string_types) and isinstance(right, float):
        return (float(left), right)
    elif isinstance(left, float) and isinstance(right, string_types):
        return (left, float(right))
    elif isinstance(left, string_types) and isinstance(right, bool):
        return (to_bool(left), right)
    elif isinstance(left, bool) and isinstance(right, string_types):
        return (left, to_bool(right))
    elif isinstance(left, integer_types) and isinstance(right, bool):
        return (bool(left), right)
    elif isinstance(left, bool) and isinstance(right, integer_types):
        return (left, bool(right))
    elif isinstance(left, float) and isinstance(right, bool):
        return (bool(int(left)), right)
    elif isinstance(left, bool) and isinstance(right, float):
        return (left, bool(int(right)))
    elif hasattr(left, '__iter__') and hasattr(right, '__iter__'):

        nl = []
        nr = []
        if len(left) == len(right):
            for i in range(len(left)):
                l, r = comparable(left[i], right[i], case_sensitive)
                nl.append(l)
                nr.append(r)
        else:
            for i in range(len(left)):
                l, _ = comparable(left[i], None, case_sensitive)
                nl.append(l)
            for i in range(len(right)):
                r, _ = comparable(right[i], None, case_sensitive)
                nr.append(r)

        return(nl, nr)
    else:
        return(left, right)
