#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

from tocoli.ratio import similarity as sim
from tocoli.cmp import comparable


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
