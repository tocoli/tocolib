#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>


from tocoli import iteritems, itervalues


def identity(x):
    return x


def identities(*args):
    return args


def identities_kwargs(**kwargs):
    return kwargs


def identities_args_kwargs(*args, **kwargs):
    return args, kwargs


def identity_values(*args, **kwargs):
    return args + tuple(v for v in itervalues(kwargs))


def return_first_value(**kwargs):
    for k in kwargs:
        return kwargs[k]
    return None


def return_values_as_tuple(**kwargs):
    return (kwargs[k] for k in kwargs)


def true(*args, **kwargs):
    return True


def false(*args, **kwargs):
    return False


def yes(*args, **kwargs):
    return True


def no(*args, **kwargs):
    return False


def first_arg(*args):
    return args[0]


def second_arg(*args):
    return args[1]


def third_arg(*args):
    return args[2]


def last_arg(*args):
    return args[-1]


def first(ordered):
    return ordered[0]


def second(ordered):
    return ordered[1]


def third(ordered):
    return ordered[2]


def last(ordered):
    return ordered[-1]


def key(iterable, value=None, sort=False, reverse=False, first=False, position=0):
    """Generic key getter. Returns one or more keys."""
    if value is None:
        return iterable[position]
    else:
        r = list(k for (k, v) in iteritems(iterable) if v == value)

        if sort:
            r = sorted(r, reverse=reverse)

        if first:
            return r[position]
        else:
            return r


def value(iterable, key=None, position=1):
    """Generic value getter. Returns containing value."""
    if key is None:
        if hasattr(iterable, '__iter__'):
            return iterable[position]
        else:
            return iterable
    else:
        return iterable[key]
