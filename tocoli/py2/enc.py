#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tocoli import Py
from codecs import encode as enc, decode as dec
from chardet import detect as det


def encode(input, output_encoding='utf-8', errors='strict', input_encoding='utf-8'):
    """Encode any string. Returns an encoded 'str' otherwise the input."""
    if isinstance(input, str):
        if input_encoding == output_encoding:
            return input
        elif input_encoding == Py.Enc.default:
            try:
                return enc(unicode(input, Py.Enc.default), output_encoding, errors)
            except:
                return enc(input, output_encoding, errors)
        else:
            try:
                return enc(unicode(dec(input, input_encoding), Py.Enc.default), output_encoding, errors)
            except:
                return enc(dec(input, input_encoding), output_encoding, errors)
    elif isinstance(input, unicode):
        if input_encoding == Py.Enc.default:
            try:
                return enc(input, output_encoding, errors)
            except:
                return enc(enc(input, Py.Enc.default, errors), output_encoding, errors)
        else:
            return encode(enc(input, 'latin-1', errors), output_encoding, errors, input_encoding)
    else:
        return input


def decode(input, encoding='utf-8', errors='strict', detect='utf-8'):
    """Decode any string. Returns a decoded 'unicode' otherwise the input."""
    if isinstance(input, str):
        try:
            r = dec(input, encoding, errors)
        except:
            r = dec(input, det(input)['encoding'], errors)

        if isinstance(r, str):
            return decode(r, detect, errors, detect)
        else:
            return r.replace(u'\ufeff', '', 1)
    elif isinstance(input, unicode):
        if encoding == Py.Enc.default:
            return input
        else:
            return decode(enc(input, 'latin-1'), encoding, errors, detect)
    else:
        return input
