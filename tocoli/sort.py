#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

from tocoli.fn import first_kwarg

ASCENDING = False
DESCENDING = True

def sort_dict_by_key(d, reverse=False):
    """Returns a 'list' of tuple(key, value)."""
    from collections import OrderedDict
    from tocoli import PY2

    def key(t):
        return t[0]

    if PY2:
        return sorted(OrderedDict(d).iteritems(), key=key, reverse=reverse)
    else:
        return sorted(OrderedDict(d).items(), key=key, reverse=reverse)


def sort_dict_by_value(d, reverse=False):
    """Returns a 'list' of tuple(key, value)."""
    from collections import OrderedDict
    from tocoli import PY2

    def value(t):
        return t[1]

    if PY2:
        return sorted(OrderedDict(d).iteritems(), key=value, reverse=reverse)
    else:
        return sorted(OrderedDict(d).items(), key=value, reverse=reverse)


def sort_dicts_by_value(iterable, keys, values=first_kwarg, default=None, sequentially=True, reverse=False):
    """Sort a list of dictionaries as you like!

    Sort a 'list' of 'dict' by value. For simple sorting define `keys` as
    'list' of 'str', where the strings are keynames. The functional `values`
    parameter behaves like the functional `key` parameter from the built-in
    `sorted` function.

    Examples:

        Simple sort by a key:

            >>> dicts = [{'name': 'Eve'},
                         {'name': 'Alice', 'email': 'alice@example.com'},
                         {'email': 'bob@example.com', 'name': 'Bob'}]

            >>> sort_dicts_by_value(dicts, ['name'])
            [{'name': 'Alice', 'email': 'alice@example.com'},
             {'email': 'bob@example.com', 'name': 'Bob'},
             {'name': 'Eve'}]

        Advanced sort for multiple keys and custom ``values`` function:

            >>> dicts = [{'price': 100},
                         {'price': 50, 'shipping': 40},
                         {'shipping': 5, 'price': 55}]

            >>> def total(price, shipping):
                    return price + shipping

            >>> sort_dicts_by_value(dicts,
                                    ['price', 'shipping'],
                                    values=total,
                                    default=0,
                                    sequentially=False)
            [{'price': 55, 'shipping': 5},
             {'price': 50, 'shipping': 40},
             {'price': 100}]

        Sort dictionaries with non string keys:

            >>> dicts = [{1: False},
                         {'right': True, 1: False},
                         {1: True, 'right': True}]

            >>> def both(left, right):
                    return left and right

            >>> sort_dicts_by_value(dicts,
                                    [{'key': 1, 'alias': 'left'}, 'right'],
                                    values=both,
                                    default=False,
                                    sequentially=False,
                                    reverse=True)
            [{1: True, 'right': True},
             {1: False},
             {1: False, 'right': True}]

    Args:
        iterable (list(dict)): The input dictonaries.

        keys (list(string or dict)): Sort by defined keys.
            If you have non string keys then `keys` should be a 'dict'
            instead of a 'list' with plain keys, which defines an alternative
            keyname for the non string key (e.g. ``keys={'key': 1: alias:
            'one'}`` instead of ``keys=[1]``). **Note:** Those dictionaries
            which do not contain any key of `keys` will be removed from the
            result.

            Options:
                - ``'key'``: defines the key
                - ``'alias'``: alternative keyname for non string key names
                - ``'sort'``: sort order (``ASCENDING`` or ``DESCENDING``)

        values (function(**kwargs) -> value): Returns the value to sort by.
            Defaults to the first value of given keywords (unordered). The
            `values` function receives the defined keys as ``**kwargs``. Thus
            it is possible to process the values easily by their name (e.g.
            ``lambda firstname, lastname: firstname + ' ' + lastname``).
            **Note:** Take the `default` and the `sequentially` parameter into
            account, when you specify a custom `values` function. In
            sequential mode you have to expect different keywords (e.g.
            ``lambda **kwargs: …``).

        default (value): Default value. Defaults to ``None``.
            Defines the default value which is passed to the ``values``
            function if a specified key from ``keys`` is not present or
            ``None``.

        sequentially (bool): Run in sequence. Defaults to True.
            If ``True`` each key in ``keys`` gets sorted one after the other
            else runs in batch mode and passes all ``keys`` to the ``values``
            function. **Note:** The keys get sorted in reverse order. Thus
            the first key gets sorted as last and vice versa.

        reverse (bool): Reverse sorting. Defaults to False.
            Reverses sotring order for each key of `keys` idependently if the
            `sequentially` parameter is ``True`` else reverses the sorted
            'list' as whole.

    Returns:
        list: A 'list' of 'dict'.
            **Note:** Those dictionaries which do not contain any key of
            `keys` will be removed from the result.

    """
    from collections import OrderedDict

    def where(d):
        return any(
            k['key'] in d
                if isinstance(k, dict) else
            k in d
            for k in keys)

    def key(d):
        return values(**OrderedDict((
                (k['alias'] if 'alias' in k else k['key'], default)
                    if not k['key'] in d or d[k['key']] is None else
                (k['alias'] if 'alias' in k else k['key'], d[k['key']])
            ) if isinstance(k, dict) else (
                (k, default)
                    if not k in d or d[k] is None else
                (k, d[k])
            ) for k in keys))

    if sequentially:
        for k in reversed(keys):
            if isinstance(k, dict) and 'sort' in k:
                if reverse:
                    iterable = sort_dicts_by_value(
                        iterable, [k], values, default, False, not k['sort'])
                else:
                    iterable = sort_dicts_by_value(
                        iterable, [k], values, default, False, k['sort'])
            else:
                iterable = sort_dicts_by_value(
                    iterable, [k], values, default, False, reverse)
        return iterable
    else:
        return sorted((d for d in filter(where, iterable)), key=key, reverse=reverse)


def sort_dicts_by_similarity(iterable,
                             keyword,
                             keys,
                             values=first_kwarg,
                             default=None,
                             sequentially=True,
                             reverse=False,
                             weights=(1, 1),
                             case_sensitive=False):
    """Returns a sorted 'list' of 'dict'."""
    from tocoli.ratio import similarity as sim

    def similarity(**kwargs):
        return sim(values(**kwargs), keyword, weights, case_sensitive)

    return sort_dicts_by_value(iterable, keys, similarity, default, sequentially, not reverse)


def sort_strings_by_similarity(iterable, keyword, reverse=False, weights=(1,1), case_sensitive=False):
    """Returns a sorted 'list'."""
    from tocoli.ratio import similarity as sim

    def similarity(value):
        return sim(value, keyword, weights, case_sensitive)

    return sorted(iterable, key=similarity, reverse=reverse)


def sort_string(s, key=None, reverse=False):
    """Returns a string."""
    return u''.join(sorted(s, key=key, reverse=reverse))


def sort_bytes(b, key=None, reverse=False, encoding='utf-8'):
    """Returns bytes."""
    from tocoli.enc import encode
    return encode(u''.join(sorted(b, key=key, reverse=reverse)), encoding)


def sort_iter(i, key=None, reverse=False):
    """Returns a list."""
    return sorted(i, key=key, reverse=reverse)


def sort_list(l, key=None, reverse=False):
    """Returns a list."""
    return sorted(l, key=key, reverse=reverse)


def sort_tuple(t, key=None, reverse=False):
    """Returns a list."""
    return sorted(t, key=key, reverse=reverse)


def sort_set(s, key=None, reverse=False):
    """Returns a list."""
    return sorted(s, key=key, reverse=reverse)
