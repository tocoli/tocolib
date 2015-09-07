#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

from tocoli import PY2


class Filter:
    @staticmethod
    def string(s, where):
        """Returns a string."""
        return u''.join(filter(where, s))

    @staticmethod
    def bytes(s, where, encoding='utf-8'):
        """Returns bytes."""
        if PY2:
            return bytes(u''.join(filter(where, s)))
        else:
            return bytes(u''.join(filter(where, s)), encoding)

    @staticmethod
    def list(l, where):
        """Returns a list."""
        return list(filter(where, l))

    @staticmethod
    def iter(i, where):
        """Returns a list."""
        return list(filter(where, i))

    @staticmethod
    def tuple(t, where):
        """Returns a list."""
        return list(filter(where, t))

    @staticmethod
    def set(s, where):
        """Returns a set."""
        return set(filter(where, s))

    class Dict:
        class by:
            @staticmethod
            def key(d, keys, all_keys=False):
                """Returns this 'dict' when it contains at least one of the specified
                `keys` else None."""
                from tocoli.filter import filter_dicts_by_keys
                try:
                    return filter_dicts_by_keys([d], keys, all_keys)[0]
                except:
                    return None

            @staticmethod
            def value(d, keywords, keys=None, all_keys=False):
                """Returns this 'dict' when it contains at least one of the keywords as
                value in the specified `keys` else None."""
                from tocoli.filter import filter_dicts_by_values
                try:
                    return filter_dicts_by_values([d], keywords, keys, all_keys)[0]
                except:
                    return None

    class Strings:
        class by:
            @staticmethod
            def similarity(iterable, keywords, ratio=0.80, weights=(1, 4), case_sensitive=False):
                """Filter strings by similar keywords. Returns a new list of strings."""
                from tocoli.filter import filter_strings_by_similarity
                return filter_strings_by_similarity(iterable, keywords, ratio, weights, case_sensitive)

            @staticmethod
            def keywords(iterable, keywords, case_sensitive=False):
                """Filter strings by exact keywords. Returns a new list."""
                from tocoli.filter import filter_strings_by_keywords
                return filter_strings_by_keywords(iterable, keywords, case_sensitive)

    class Dicts:
        class by:

            @staticmethod
            def key(iterable, keys, all_keys=False):
                """Returns a 'list' of 'dict' whose dictionaries contain at least one of
                the specified `keys`."""
                from tocoli.filter import filter_dicts_by_keys
                return filter_dicts_by_keys(iterable, keys, all_keys)

            @staticmethod
            def value(iterable, keywords, keys=None, all_keys=False):
                """Returns a 'list' of 'dict' whose dictionaries contain at least one of
                the keywords as value in the specified `keys`."""
                from tocoli.filter import filter_dicts_by_values
                return filter_dicts_by_values(iterable, keywords, keys, all_keys)


class Sort:

    @staticmethod
    def string(s, key=None, reverse=False):
        """Returns a string."""
        return u''.join(sorted(s, key=key, reverse=reverse))

    @staticmethod
    def bytes(b, key=None, reverse=False, encoding='utf-8'):
        """Returns bytes."""
        if PY2:
            return bytes(u''.join(sorted(b, key=key, reverse=reverse)))
        else:
            return bytes(u''.join(sorted(b, key=key, reverse=reverse)), encoding)

    @staticmethod
    def list(l, key=None, reverse=False):
        """Returns a list."""
        return sorted(l, key=key, reverse=reverse)

    @staticmethod
    def iter(i, key=None, reverse=False):
        """Returns a list."""
        return sorted(i, key=key, reverse=reverse)

    @staticmethod
    def tuple(t, key=None, reverse=False):
        """Returns a list."""
        return sorted(t, key=key, reverse=reverse)

    @staticmethod
    def set(s, key=None, reverse=False):
        """Returns a list."""
        return sorted(s, key=key, reverse=reverse)

    class Dict:
        class by:
            @staticmethod
            def key(d, reverse=False):
                """Returns a 'list' of tuple(key, value)."""
                from tocoli.sort import sort_dict_by_key
                return sort_dict_by_key(d, reverse)

            @staticmethod
            def value(d, reverse=False):
                """Returns a 'list' of tuple(key, value)."""
                from tocoli.sort import sort_dict_by_value
                return sort_dict_by_value(d, reverse)

    class Strings:
        class by:
            @staticmethod
            def similarity(iterable, keyword, reverse=False, weights=(1,1), case_sensitive=False):
                """Returns a sorted 'list' of strings."""
                from tocoli.sort import sort_strings_by_similarity
                return sort_strings_by_similarity(iterable, keyword, reverse, weights, case_sensitive)

    class Dicts:
        class by:
            from tocoli.fn import return_first_value
            @staticmethod
            def value(iterable, keys, values=return_first_value, default=None, reverse=False):
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
                from tocoli.sort import sort_dicts_by_value
                return sort_dicts_by_value(iterable, keys, values, default, reverse)


            @staticmethod
            def similarity(iterable,
                             keyword,
                             keys,
                             values=return_first_value,
                             default=None,
                             reverse=False,
                             weights=(1, 1),
                             case_sensitive=False):
                """Returns a sorted 'list' of 'dict'."""
                from tocoli.sort import sort_dicts_by_similarity
                return sort_dicts_by_similarity(iterable,
                                                 keyword,
                                                 keys,
                                                 values,
                                                 default,
                                                 reverse,
                                                 weights,
                                                 case_sensitive)


class Map:
    from tocoli.map import (identity,
                            MAP_NONE,
                            MAP_NUMERIC,
                            MAP_STR,
                            MAP_LIST,
                            MAP_TUPLE,
                            MAP_SET,
                            MAP_DICT_KEY,
                            MAP_DICT_VALUE,
                            MAP_DICT,
                            MAP_OTHER,
                            MAP_ALL,
                            MAP_DEFAULT)

    @staticmethod
    def any(item, function=identity, flags=MAP_DEFAULT):
        """ Maps any function recursivly to the item. """
        from tocoli.map import map
        return map(item, function, flags)


class Join:
    class Strings:
        class by:
            @staticmethod
            def keywords(list, keywords, join=' '):
                """Join strings by keywords. Returns a new list with joined strings."""
                from tocoli.join import join_strings_by_keywords
                return join_strings_by_keywords(list, keywords, join)

