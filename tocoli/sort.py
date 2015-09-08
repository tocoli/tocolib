#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

from tocoli import PY2
from tocoli.join import join_values_as_string


def sort_dict_by_key(d, reverse=False):
    """Returns a 'list' of tuple(key, value)."""
    from collections import OrderedDict
    def key(t):
        return t[0]

    if PY2:
        return sorted(OrderedDict(d).iteritems(), key=key, reverse=reverse)
    else:
        return sorted(OrderedDict(d).items(), key=key, reverse=reverse)


def sort_dict_by_value(d, reverse=False):
    """Returns a 'list' of tuple(key, value)."""
    from collections import OrderedDict
    def value(t):
        return t[1]

    if PY2:
        return sorted(OrderedDict(d).iteritems(), key=value, reverse=reverse)
    else:
        return sorted(OrderedDict(d).items(), key=value, reverse=reverse)


def sort_dicts_by_value(iterable, keys, values=join_values_as_string, default=None, reverse=False):
    """Sort a list of dictionaries as you like!

    Sort dictionaries which are in a 'list'. The functional `where` parameter
    behaves like the filter function from the built-in `filter` function. The
    functional `key` parameter behaves like the functional `key` parameter
    from the built-in `sorted` function.

    Examples:

        Simple sort by a key:

            >>> dicts = [{'name': 'Eve'},
                         {'name': 'Alice', 'email': 'alice@example.com'},
                         {'email': 'bob@example.com', 'name': 'Bob'}]

            >>> sort_dictionaries(dicts, ['name'])
            [{'name': 'Alice', 'email': 'alice@example.com'},
             {'email': 'bob@example.com', 'name': 'Bob'},
             {'name': 'Eve'}]

        Advanced sort for multiple keys with custom sort value:

            >>> dicts = [{'price': 100},
                         {'price': 50, 'shipping': 40},
                         {'shipping': 5, 'price': 55}]

            >>> def total(price, shipping):
                    return price + shipping

            >>> sort_dictionaries(dicts,
                                  ['price', 'shipping'],
                                  values=total,
                                  default=0)
            [{'price': 55, 'shipping': 5},
             {'price': 50, 'shipping': 40},
             {'price': 100}]

        Sort dictionaries with non string keys:

            >>> dicts = [{1: False},
                         {2: True, 1: False},
                         {1: True, 2: True}]

            >>> def both(left, right):
                    return left and right

            >>> sort_dictionaries(dicts,
                                  {1: 'left', 2: 'right'}
                                  values=both,
                                  default=False,
                                  reverse=True)
            [{1: True, 2: True}, {1: False}, {1: False, 2: True}]

    Args:
        iterable (list(dict)): The input dictonaries.

        keys (list or dict): Sort by defined keys.
            If you have non string keys then `keys` should be a 'dict' instead
            of a 'list' with keys, which defines an alternative string repre-
            sentation for the non string key (e.g. keys={1: 'one'} instead of
            keys=[1]).
            If none of the `keys` is present in a 'dict', than it will be re-
            moved from the result.

        values (function(**kwargs) -> value): Returns the value to sort by.
            Defaults to the first value if not specified. The `values` func-
            tion receives the defined `keys` as **kwargs. Thus it is possible
            to process the values easily by their key name (e.g. lambda a, b:
             a + b).

        default (value): Default value value. Defaults to None.
            Defines the default value if a specified key from `keys` is not
            present or None.

        reverse (bool): Reverse the output list.

    Returns:
        list: A 'list' of 'dict'.
            If none of the `keys` is present in a 'dict', than it will be re-
            moved from the result.

    """

    def where(d):
        return any(k in d for k in keys)

    def key(d):
        if isinstance(keys, dict):
            return values(**{keys[k]: d[k]
                            if k in d and d[k] is not None else
                          default
                            for k in keys})
        else:
            return values(**{k: d[k]
                            if k in d and d[k] is not None else
                          default
                            for k in keys})

    return sorted(
        (d for d in filter(where, iterable)), key=key, reverse=reverse)


def sort_dicts_by_similarity(iterable,
                             keyword,
                             keys,
                             values=join_values_as_string,
                             default=None,
                             reverse=False,
                             weights=(1, 1),
                             case_sensitive=False):
    """Returns a sorted 'list' of 'dict'."""
    from tocoli.ratio import similarity as sim

    def similarity(**kwargs):
        return sim(values(**kwargs), keyword, weights, case_sensitive)

    return sort_dicts_by_value(iterable, keys, similarity, default, reverse)


def sort_strings_by_similarity(iterable, keyword, reverse=False, weights=(1,1), case_sensitive=False):
    """Returns a sorted 'list'."""
    from tocoli.ratio import similarity as sim

    def similarity(value):
        return sim(value, keyword, weights, case_sensitive)

    return sorted(iterable, key=similarity, reverse=reverse)

