#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

from tocoli.ratio import similarity as sim
from tocoli.cmp import comparable
from tocoli.enc import encode


def filter_strings_by_similarity(iterable, keywords, ratio=0.80, weights=(1, 4), case_sensitive=False):
    """Filter strings by similar keywords. Returns a new list of strings."""

    its, keys = comparable(iterable, keywords, case_sensitive)

    return [iterable[i] for i, s in enumerate(its)
                            for key in keys
                                if sim(s, key, weights=weights) >= ratio]


def filter_strings_by_keywords(iterable, keywords, case_sensitive=False):
    """Filter strings by exact keywords. Returns a new list."""

    its, keys = comparable(iterable, keywords, case_sensitive)

    return [iterable[i] for i, s in enumerate(its)
                            for k in keys
                                if s == k]


def filter_dicts_by_keys(iterable, keys, all_keys=False):
    """Returns a 'list' of 'dict' whose dictionaries contain at least one of
    the specified `keys`."""
    def where(d):
        if all_keys:
            return all(k in d for k in keys)
        else:
            return any(k in d for k in keys)
    return [x for x in filter(where, iterable)]


def filter_dicts_by_values(iterable, keywords, keys=None, all_keys=False):
    """Returns a 'list' of 'dict' whose dictionaries contain at least one of
       the keywords as value in the specified `keys`."""

    def where(d, keys=keys):
        if keys is None:
            keys = d.keys()

        if all_keys:
            return all( d[k] in keywords
                            if k in d else
                        False
                            for k in keys)
        else:
            return any( d[k] in keywords
                            if k in d else
                        False
                            for k in keys)

    return [x for x in filter(where, iterable)]


def filter_dict_by_key(d, keys, all_keys=False):
    """Returns this 'dict' when it contains at least one of the specified
    `keys` else None."""
    try:
        return filter_dicts_by_keys([d], keys, all_keys)[0]
    except:
        return None


def filter_dict_by_value(d, keywords, keys=None, all_keys=False):
    """Returns this 'dict' when it contains at least one of the keywords as
    value in the specified `keys` else None."""
    try:
        return filter_dicts_by_values([d], keywords, keys, all_keys)[0]
    except:
        return None


def clean(str, include='', alpha='a-zA-Z', numeric='0-9'):
    """Filter unwanted characters. Returns the filtered string.

        Examples:

            >>> clean('1.20€')
            '120'

            >>> clean('1.20€', '.')
            '1.20'

            >>> clean('1.20€', '.€')
            '1.20€'

            >>> clean('Hello', alpha='a-z')
            'ello'

        Args:
            str (str): input string
            include (str): Regular-expression raw string. Defaults to ''.
                This parameter defines which additional characters to include
                to the result.
            alpha (str): Regular-expression raw string. Defaults to 'a-zA-Z'.
                This parameter defines which alpha characters should be in the
                result.
            numeric (str): Regular-expression raw string. Defaults to '0-9'.
                This parameter defines which numeric characters should be in
                the result.

        Returns:
            str: string which only contains accepted characters.

    """
    import re
    return re.sub('[^{}{}{}]+'.format(alpha, numeric, include), '', str)


def filter_string(s, where):
    """Returns a string."""
    return u''.join(filter(where, s))


def filter_bytes(s, where, encoding='utf-8'):
    """Returns bytes."""
    return encode(u''.join(filter(where, s)), encoding)


def filter_list(l, where):
    """Returns a list."""
    return list(filter(where, l))


def filter_iter(i, where):
    """Returns a list."""
    return list(filter(where, i))


def filter_tuple(t, where):
    """Returns a list."""
    return list(filter(where, t))


def filter_set(s, where):
    """Returns a set."""
    return set(filter(where, s))
