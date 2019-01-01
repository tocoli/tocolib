#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from tocoli.spell import lookup
from tocoli import PY2, string_types





# Character classes

ANY = r'.'
WORD = r'\w'
NOT_WORD = r'\W'
DIGIT = r'\d'
NOT_DIGIT = r'\D'
WHITESPACE = r'\s'
NOT_WHITESPACE = r'\S'

class CharClass:
    ANY = ANY
    WORD = WORD
    NOT_WORD = NOT_WORD
    DIGIT = DIGIT
    NOT_DIGIT = NOT_DIGIT
    WHITESPACE = WHITESPACE
    NOT_WHITESPACE = NOT_WHITESPACE


def set(chars, expr=None):
    if PY2:
        from __builtin__ import range
        chars = unicode(chars)
    else:
        from builtins import range
        chars = str(chars)

    p = re.compile(r'(\\?.-\\?.|\\.)')
    rs = p.findall(chars)
    for r in rs:
        chars = chars.replace(r, '')
    for r in rs:
        for c in chars:
            if ord(c) in range(ord(r[0]), ord(r[2])+1):
                chars = chars.replace(c, '')
    s = u'[{}]'.format(u''.join(sorted(rs) + sorted({c for c in chars})))
    if expr is None:
        return Re(s)
    else:
        return Re(expr + s)


def negated_set(chars, expr=None):
    if PY2:
        from __builtin__ import range
        chars = unicode(chars)
    else:
        from builtins import range
        chars = str(chars)

    p = re.compile(r'(\\?.-\\?.|\\.)')
    rs = p.findall(chars)
    for r in rs:
        chars = chars.replace(r, '')
    for r in rs:
        for c in chars:
            if ord(c) in range(ord(r[0]), ord(r[2])+1):
                chars = chars.replace(c, '')
    s = u'[^{}]'.format(u''.join(sorted(rs) + sorted({c for c in chars})))
    if expr is None:
        return Re(s)
    else:
        return Re(expr + s)


def range(start, end):
    if isinstance(start, int):
        start = str(start)
    if isinstance(end, int):
        end = str(end)
    sl = start.lower()
    el = end.lower()
    su = start.upper()
    eu = end.upper()
    if start == sl and end == el:
        return u'{}-{}'.format(start, end)
    elif start == su and end == eu:
        return u'{}-{}'.format(start, end)
    else:
        return u'{}-{}{}-{}'.format(sl, el, su, eu)


# Anchors
BEGINNING = r'^'
END = r'$'
WORD_BOUNDARY = r'\b'
NOT_WORD_BOUNDARY = r'\B'

class Anchors:
    BEGINNING = BEGINNING
    END = END
    WORD_BOUNDARY = WORD_BOUNDARY
    NOT_WORD_BOUNDARY = NOT_WORD_BOUNDARY

# Escaped characters
def escape_octal(triplet):
    from string import octdigits
    if PY2:
        from __builtin__ import range
    else:
        from builtins import range

    if not isinstance(triplet, string_types):
        triplet = oct(triplet)
        if PY2:
            triplet = triplet if len(triplet) == 1 else triplet[1:]
        else:
            triplet = triplet if len(triplet) == 1 else triplet[2:]

    lt = len(triplet)
    if lt > 3:
        raise ValueError(u'octal has more than three digits: {}'.format(triplet))
    elif lt < 3:
        zeros = u''.join('0' for _ in range(3-lt))
        triplet = u'{}{}'.format(zeros, triplet)

    if not all(oct in octdigits for oct in triplet):
        raise ValueError(u'invalid literal for octal: \'{}\''.format(triplet))

    return Re(u'\\{}'.format(triplet))

def escape_hexadecimal(pair):
    from string import hexdigits
    if PY2:
        from __builtin__ import range
    else:
        from builtins import range

    if not isinstance(pair, string_types):
        pair = hex(pair)
        pair = pair if len(pair) == 1 else pair[2:]

    lt = len(pair)
    if lt > 2:
        raise ValueError(u'hex has more than two digits: {}'.format(pair))
    elif lt < 2:
        zeros = u''.join('0' for _ in range(2-lt))
        pair = u'{}{}'.format(zeros, pair)

    if not all(hex in hexdigits for hex in pair):
        raise ValueError(u'invalid literal for hex: \'{}\''.format(pair))

    return Re(u'\\x{}'.format(pair.upper()))

def escape_unicode(quadruple):
    from string import hexdigits
    if PY2:
        from __builtin__ import range
    else:
        from builtins import range

    if not isinstance(quadruple, string_types):
        quadruple = hex(quadruple)
        quadruple = quadruple if len(quadruple) == 1 else quadruple[2:]

    lt = len(quadruple)
    if lt > 4:
        raise ValueError(u'hex has more than four digits: {}'.format(quadruple))
    elif lt < 4:
        zeros = u''.join('0' for _ in range(4-lt))
        quadruple = u'{}{}'.format(zeros, quadruple)

    if not all(hex in hexdigits for hex in quadruple):
        raise ValueError(u'invalid literal for hex: \'{}\''.format(quadruple))

    return Re(u'\\u{}'.format(quadruple.upper()))

def escape_control_char(char):
    if not isinstance(char, string_types):
        char = chr(char)

    char = char.upper()

    if char < 'A':
        raise ValueError(
            u'control character should be bigger than \'A\'({}): \'{}\'({})'.
                format(ord('A'), char, ord(char)))

    if char > 'Z':
        raise ValueError(
            u'control character should be smaller than \'Z\'({}): {}({})'.
                format(ord('Z'), char, ord(char)))


    return u'\\c{}'.format(char)

def escape(expr):
    return Re(re.escape(expr))

class Escaped:
    TAB = r'\t'
    LINE_FEED = r'\n'
    VERTICAL_TAB = r'\v'
    FORM_FEED = r'\f'
    CARRIAGE_RETURN = r'\r'
    NULL = r'\0'

# Groups & Lookaround

def group_capturing(expr):
    return Re(u'({})'.format(expr))

def group_non_capturing(expr):
    return Re(u'(?:{})'.format(expr))

def group(expr, capturing=True):
    if capturing:
        return group_capturing(expr)
    else:
        return group_non_capturing(expr)

def backreference(n):
    if not isinstance(n, int):
        raise TypeError(u'n must be <type int>: {}'.format(type(n)))
    if n < 0:
        raise ValueError(u'n must be positive: {}'.format(n))
    return Re(u'\\{}'.format(n))

def lookahead_positive(expr, lookup):
    return Re(u'{}(?={})'.format(expr, lookup))

def lookahead_negative(expr, lookup):
    return Re(u'{}(?!{})'.format(expr, lookup))

def lookahead(expr, lookup, positive=True):
    if positive:
        return lookahead_positive(expr, lookup)
    else:
        return lookahead_negative(expr, lookup)

def lookbehind_positive(expr, lookup):
    return Re(u'{}(?<={})'.format(expr, lookup))

def lookbehind_negative(expr, lookup):
    return Re(u'{}(?<!{})'.format(expr, lookup))

def lookbehind(expr, loookup, positive=True):
    if positive:
        return lookbehind_positive(expr, loookup)
    else:
        return lookbehind_negative(expr, loookup)

# Quantifieres & Alternation

PLUS = r'+'
STAR = r'*'
OPTIONAL = r'?'

class Quantifier:
    PLUS = PLUS
    STAR = STAR
    OPTIONAL = OPTIONAL

def plus(expr):
    return QuantifiedRe(u'{}+'.format(expr))

def star(expr):
    return QuantifiedRe(u'{}*'.format(expr))

def optional(expr):
    return QuantifiedRe(u'{}?'.format(expr))

def quantify(expr, min, max=None):
    if not isinstance(min, int):
        int(min)

    if max is None or max is False:
        max = ''
    else:
        if not isinstance(max, int) and max != '':
            int(max)

    return QuantifiedRe(u'{}{}{},{}{}'.format(expr, u'{', min, max, u'}'))

def quantify_lazy(expr, min, max=None):
    return Re(u'{}?'.format(quantify(expr, min, max)))


def lazy(quantified_expr):
    # if not isinstance(quantified_expr, QuantifiedRe):
    #     raise TypeError(u'must be a <type QuantifiedRe>: {}'.format(type(quantified_expr)))
    return Re(u'{}?'.format(quantified_expr))


ALTERNATION = r'|'

def alternate(left, right):
    return u'{}|{}'.format(left, right)

# Substitution

class Substitution:
    MATCH = r'$&'
    BEFORE_MATCH = r'$`'
    AFTER_MATCH = r"$'"
    DOLLAR = r'$$'

    def capture_group(n):
        return r'${}'.format(n)

# Flags

class Flags:
    IGNORE_CASE = 'i'
    GLOBAL_SEARCH = 'g'
    MULTILINE = 'm'


class Re(unicode if PY2 else str):

    def __init__(self, expr=None):
        if expr is None:
            self.expr = u''
        else:
            if PY2:
                self.expr = unicode(expr)
            else:
                self.expr = str(expr)

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __hash__(self):
        return hash(self.expr)

    def __add__(self, other):
        return Re(u'{}{}'.format(self.expr, other.expr))

    def __and__(self, other):
        return Re(u'{}{}'.format(self.expr, other.expr))

    def __or__(self, other):
        return Re(u'{}|{}'.format(self, other))

    def __coerce__(self, other):
        if not isinstance(self, Re):
            self = Re(repr(self))
        if not isinstance(self, Re):
            other = Re(repr(other))
        return (self, other)

    def add_set(self, chars):
        return self + set(chars)

    def add_negated_set(self, chars):
        return self + negated_set(chars)

    def set(self, chars=None):
        return set(self.expr + (chars if chars is not None else ''))

    def negated_set(self):
        return negated_set(self.expr)

    def add_escaped_octal(self, triplet):
        return self + escape_octal(triplet)

    def add_escaped_hexadecimal(self, pair):
        return self + escape_hexadecimal(pair)

    def add_escaped_unicode(self, quadruple):
        return self + escape_unicode(quadruple)

    def add_escaped_control_char(self, char):
        return self + escape_control_char(char)

    def add(self, expr, escape=False):
        if escape:
            return self + escape(expr)
        else:
            return self + Re(expr)

    def escape(self):
        return escape(self.expr)

    def group(self, capturing=True):
        return group(self.expr, capturing)

    def add_backreference(self, n):
        return self + backreference(n)

    def lookahead(self, lookup, positive=True):
        return lookahead(self.expr, lookup, positive)

    def lookbehind(self, lookup, positive=True):
        return lookbehind(self.expr, lookup, positive)

    def plus(self):
        return plus(self.expr)

    def star(self):
        return star(self.expr)

    def optional(self):
        return optional(self.expr)

    def quantify(self, min, max=None):
        return quantify(self.expr, min, max)


class QuantifiedRe(Re):

    def lazy(self):
        return lazy(self.expr)



class Generator():

    def __init__(self, options, dictionary):
        self.options = options

    def generate(self, input):
        pass


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
