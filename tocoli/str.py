#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import locale
# import os
# import unicodedata
import codecs
import sys
import py2.str as py2str
import py3.str as py3str

encoding = locale.getpreferredencoding()
version  = sys.version_info[0]

def decode(value, encoding=encoding):

    if version == 2:
        return py2str.decode(value, encoding)
    elif version == 3:
        return py3str.decode(value, encoding)
    else:
        try:
            return py3str.str.decode(value, encoding)
        except:
            raise RuntimeError('decode(): ' + sys.version + 'is not supported')

def encode(value, encoding=encoding):
    if version == 2:
        return py2str.encode(value, encoding)
    elif version == 3:
        return py3str.encode(value, encoding)
    else:
        try:
            return py3str.str.decode(value, encoding)
        except:
            raise RuntimeError('decode(): ' + sys.version + 'is not supported')

Writer     = codecs.getwriter(encoding)
sys.stdout = Writer(encode(sys.stdout))
