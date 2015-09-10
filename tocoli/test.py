#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

from time import time


def arguments(args=None, kwargs=None):
    r = '('

    if len(args) > 0:
        r += ', '.join(tuple("'" + v + "'"
            if isinstance(v, str) else
        v.__class__.__name__ + ' #' + str(len(v))
            if hasattr(v, '__iter__') and len(v) > 3 else
        v.__class__.__name__
            if hasattr(v, '__call__') else
        str(v)
            for v in args))

    if len(kwargs) > 0:
        if len(args) > 0:
            r += ', '
        r += ', '.join(tuple(str(k) + '=' + "'" + str(kwargs[k]) + "'"
            if isinstance(kwargs[k], str) else
        str(k) + '=' + kwargs[k].__class__.__name__ + ' #' + str(len(kwargs[k]))
            if hasattr(kwargs[k], '__iter__') and len(kwargs[k]) > 3 else
        str(k) + '=' + kwargs[k].__class__.__name__
            if hasattr(kwargs[k], '__call__') else
        str(k) + '=' + str(kwargs[k])
            for k in sorted(kwargs)))

    r += ')'
    return r


class Bencher:

    def __init__(self, rounds=1, collect=False, stopwatch=True, precision='0.8'):
        self.rounds = rounds
        self.collect = collect
        self.stopwatch = stopwatch
        self.precision = precision

    def bench(self, function, *args, **kwargs):
        res = []

        benched = 0.0
        r = range(self.rounds)

        for _ in r:
            start = time()
            r = function(*args, **kwargs)
            end = time()
            benched += (end - start)

            if self.collect:
                res.append(r)
            else:
                res = r

        if self.stopwatch:
            print('benched: ' + function.__name__ + arguments(args, kwargs))
            print('rounds:  ' + str(self.rounds))
            print('average: ' + ('{:{}f}').format(benched / float(self.rounds), self.precision) + 's')
            print('total:   ' + ('{:{}f}').format(benched, self.precision) + 's')
            print('')

        return res

bench = Bencher().bench


def fnprint(function, *args, **kwargs):
    from pprint import pprint

    def sep(s, sep='<', width=80):
        for _ in range(width - len(s)):
            s += sep
        return s

    print('')
    print(sep('>>> ' + function.__name__ + arguments(args, kwargs) + ' '))
    res = function(*args, **kwargs)
    pprint(res)

    stat = []
    stat.append("type '" + res.__class__.__name__ + "'")
    if hasattr(res, '__iter__'):
        types = []
        for e in res:
            types.append(e.__class__.__name__)
        stat.append(list(set(types)))
    if hasattr(res, '__len__'):
        stat.append(' #' + str(len(res)))
    print(''.join(map(str, stat)))

    return res
