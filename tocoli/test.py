#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import time
import inspect


def bench(function, args, rounds=1, collect=False, stopwatch=True, precision='0.3'):
    """ Benchmark functions to test their performance. """

    res = []
    start = 0.0
    end = 0.0
    r = range(rounds)
    arg_count = len(inspect.getargspec(function).args)
    if (arg_count > 1 and hasattr(args, '__iter__')):
        start = time.time()
        for i in r:
            function(*args)
        end = time.time()

        if collect:
            for i in r:
                res.append(function(*args))
        else:
            res = function(*args)
    else:
        start = time.time()
        for i in r:
            function(args)
        end = time.time()

        if collect:
            for i in r:
                res.append(function(args))
        else:
            res = function(args)

    if stopwatch:
        print(('{:' + precision + 'f}').format(end - start) + 's')

    return res


def fnprint(function, *args, **kwargs):
    from pprint import pprint

    def sep(s, sep='<', width=80):
        for _ in range(width - len(s)):
            s += sep
        return s

    arguments = '('
    if len(args) > 0:
        arguments += ', '.join(tuple("'" + v + "'"
                                        if isinstance(v, str) else
                                     v.__class__.__name__ + ' #' + str(len(v))
                                        if hasattr(v, '__iter__') and len(v) > 3 else
                                     v.__class__.__name__
                                        if hasattr(v, '__call__') else
                                     str(v)
                                        for v in args))
    if len(kwargs) > 0:
        if len(args) > 0:
            arguments += ', '
        arguments += ', '.join(tuple(str(k) + '=' + "'" + str(kwargs[k]) + "'"
                                        if isinstance(kwargs[k], str) else
                                     str(k) + '=' + kwargs[k].__class__.__name__ + ' #' + str(len(kwargs[k]))
                                        if hasattr(kwargs[k], '__iter__') and len(kwargs[k]) > 3 else
                                     str(k) + '=' + kwargs[k].__class__.__name__
                                        if hasattr(kwargs[k], '__call__') else
                                     str(k) + '=' + str(kwargs[k])
                                        for k in sorted(kwargs)))
    arguments += ')'

    print('')
    print(sep('>>> ' + function.__name__ + arguments + ' '))
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
