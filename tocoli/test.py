#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

from time import time
from numpy import array, median


def arguments(args=None, kwargs=None):
    r = '('

    if args is not None and len(args) > 0:
        r += ', '.join(tuple("'" + v + "'"
            if isinstance(v, str) else
        v.__class__.__name__ + ' #' + str(len(v))
            if hasattr(v, '__iter__') and len(v) > 3 else
        v.__class__.__name__
            if hasattr(v, '__call__') else
        str(v)
            for v in args))

    if kwargs is not None and len(kwargs) > 0:
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


def seperator(str='', seperator='-', width=80):

    if width is None or width < 0:
        import os
        _, width = os.popen('stty size', 'r').read().split()
        width = int(width) - 1

    for _ in range(width - len(str)):
        str += seperator

    return str


class Bencher:

    def __init__(self, rounds=1, collect=False, stopwatch=True, precision='0.8'):
        self.rounds = rounds
        self.collect = collect
        self.stopwatch = stopwatch
        self.precision = precision
        self.seperator = '-'
        self.width = None

    def bench(self, function, *args, **kwargs):
        res = []

        t = 0.0
        m = None
        b = []
        r = range(self.rounds)

        for _ in r:
            start = time()
            r = function(*args, **kwargs)
            end = time()
            diff = end - start
            t += diff

            b.append(diff)
            if len(b) > 1000:
                if m is None:
                    m = median(array(b))
                else:
                    m = (m + median(array(b))) / float(2)
                b = []

            if self.collect:
                res.append(r)

        if m is None:
            m = median(array(b))
        else:
            m = (m + median(array(b))) / float(2)
        a = t / float(self.rounds)

        if self.stopwatch:
            print(seperator(seperator=self.seperator, width=self.width))
            print('benched: {}{} '.format(function.__name__, arguments(args, kwargs)))
            print('{} times '.format(self.rounds) if self.rounds > 1 else '{} time '.format(self.rounds))
            print('{:{}f}s (median) '.format(m, self.precision))
            print('{:{}f}s (average) '.format(a, self.precision))
            print('{:{}f}s (total) '.format(t, self.precision))

        if not self.collect:
            res = r
        return res

bench = Bencher().bench


class FnPrinter():

    def __init__(self, seperator='-', width=None):
        self.seperator = seperator
        self.width = width

    def fnprint(self, function, *args, **kwargs):
        from pprint import pprint

        print('')
        print(seperator(
            '>>> ' + function.__name__ + arguments(args, kwargs) + ' ',
            self.seperator,
            self.width))

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

fnprint = FnPrinter().fnprint
