#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tocoli.cmp import comparable
from Levenshtein import ratio as levenshtein


def count_equal_chars(str1, str2):
    return len(set(str1) & set(str2))


class Nominator:
    MIN = 'min'
    MAX = 'max'

def equal(str1, str2, nominator='max'):
    """A simple ratio function based on the equality."""
    e = count_equal_chars(str1, str2)

    if nominator == Nominator.MAX:
        l = max(len(str1), len(str2))
    else:
        l = min(len(str1), len(str2))

    if l == 0:
        return 1.0 if e == 0 else 0.0
    else:
        return e / float(l)


def meta(str1, str2, ratios, weights):
    """A meta ratio function. Returns a weighted meta ratio.

    The Wiesendahl ratio is a meta ratio which combines a weighted
    ratio of given ratio functions.

    Args:

        str1   (str): first string
        str2   (str): second string
        ratios (list(function(str, str) -> float)): ratio functions
            This parameter is a list of ratio functions.
        weights (list(float)): list of weights
            Each weight gets applied to its corresponding function.

    Returns:
        float: the combined and weighted meta ratio

    """

    c = 0
    r = 0.0
    for i, fn in enumerate(ratios):
        r += fn(str1, str2) * weights[i]
        c += weights[i]

    return r / float(c)


def similarity(str1, str2, weights=(1, 1), case_sensitive=True):
    s1, s2 = comparable(str1, str2, case_sensitive)
    return meta(s1, s2, ratios=(equal, levenshtein), weights=weights)


# http://stackoverflow.com/a/29870273
# https://stackoverflow.com/users/4832830/batuhan-ulug
def median(list):
    m, r = divmod(len(list), 2)
    if r:
        return sorted(list)[m]
    return sum(sorted(list)[m-1:m+1]) / 2.0
