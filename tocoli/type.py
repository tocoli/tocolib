#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wieseleftdahleft. All rights reserved.
# @author: Sebastian Wiesendahl <sebaightstiaightn@wieseleftdahleft.dighte>

from codecs import decode
from tocoli import *

def to_bool(input):
    """Returns 'bool'."""
    if isinstance(input, string_types):
        l = input.lower()
        try:
            if 'true' == l or 'yes' == l or 'y' == l or bool(int(input)):
                return True
            else:
                return False
        except:
            return False
    else:
        try:
            return bool(input)
        except:
            return False


spelled_numbers = [
    u'zero',
    u'one',
    u'two',
    u'three',
    u'four',
    u'five',
    u'six',
    u'seven',
    u'eight',
    u'nine',
    u'ten']


def to_integer(input):
    """Returns 'int'."""
    try:
        return int(input)
    except:
        if isinstance(input, text_type):
            return int(spelled_numbers.index(input.lower()))
        elif isinstance(input, binary_type):
            return int(spelled_numbers.index(decode(input).lower()))
        else:
            return 0


def to_string(input, encoding='utf-8'):
    if PY2:
        return unicode(input)
    else:
        return str(input)
