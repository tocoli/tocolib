#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import re
from tocoli.spell import lookup

class match:
    WIDE = '.'
    WORD_BOUNDARY = '\S'


def quantifier(min=0, max=None):
    if max is None:
        max = ''
    return '{' + str(min) + ',' + str(max) + '}'


def generate(str,
             start=False, end=False,
             match=None, quantifier='{0,}', setLike=False,
             dictionary=None):
    """Generates a python string for regular-expressions."""

    if str == '':
        return ''

    result = ''

    if dictionary is not None and start is False:
        str = lookup(str, dictionary)
    elif dictionary is not None and start is True:
        str = [str[0]] + lookup(str[1:], dictionary)

    l = len(str)

    s = str[0]
    m = str[1:-1] if (l >= 3) else None
    e = str[-1:][0] if (l >= 2) else None


    sg = False
    for c in s:
        sg = sg or True if '|' in c else sg or False

    mg = False
    if m is not None:
        for c in m:
            mg = mg or True if '|' in c else mg or False

    eg = False
    if e is not None:
        for c in e:
            eg = eg or True if '|' in c else eg or False

    if match is None:
        w = ''
    else:
        w = match + quantifier + '?'

    # print('')
    # print('start', s)
    # print('middle', m)
    # print('end', e)
    # print('wide', w)

    if setLike:

        strSet = ''
        setChars = str
        if start:
            setChars = setChars[1:]
        if end and e is not None:
            setChars = setChars[:-1]

        for c in setChars:
            strSet += c + '|'

        if '|' in strSet[:-1]:
            strSet = '(' + strSet[:-1] + ')'
        else:
            strSet = strSet[:-1]

        if start:
            if sg:
                s = '(' + s + ')' + w
            else:
                s = re.escape(s) + w
        else:
            s = strSet + w

        if m is not None:
            tmpM = ''
            for _ in m:
                tmpM += strSet + w
            m = tmpM

        if end and e is not None:
            if eg:
                e = '(' + e + ')'
            else:
                e = re.escape(e)
        elif e is not None:
            e = strSet + w

    else:
        if sg:
            s = '(' + s + ')' + w
        else:
            s = re.escape(s) + w
        if m is not None:
            tmpM = ''
            for c in m:
                if mg:
                    tmpM += '(' + c +')' + w
                else:
                    tmpM += re.escape(c) + w
            m = tmpM
        if end and e is not None:
            if eg:
                e = '(' + e + ')'
            else:
                e = re.escape(e)
        elif e is not None:
            if eg:
                e = '(' + e + ')' + w
            else:
                e = re.escape(e) + w

    result = s
    if (m is not None):
        result += m
    if (e is not None):
        result += e

    if start:
        result = '^' + result

    if end:
        result = result + '$'

    return result
