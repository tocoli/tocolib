#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tocoli import Py
from codecs import encode as enc, decode as dec
from chardet import detect as det


def encode(input, output_encoding='utf-8', errors='strict', input_encoding='utf-8'):
    """Encode any string. Returns encoded 'bytes' otherwise the input."""
    if isinstance(input, bytes):
        if input_encoding == output_encoding:
            return input
        elif input_encoding == Py.Enc.default:
            try:
                return enc(str(input, Py.Enc.default), output_encoding, errors)
            except UnicodeEncodeError as e:
                raise e
            except:
                return enc(input, output_encoding, errors)
        else:
            try:
                return enc(str(dec(input, input_encoding), Py.Enc.default), output_encoding, errors)
            except UnicodeEncodeError as e:
                raise e
            except:
                return enc(dec(input, input_encoding), output_encoding, errors)

    elif isinstance(input, str):
        if input_encoding == Py.Enc.default:
            try:
                return enc(input, output_encoding, errors)
            except UnicodeEncodeError as e:
                raise e
            except:
                return enc(bytes(input, Py.Enc.default), output_encoding, errors)
        else:
            return encode(enc(input, 'latin-1', errors), output_encoding, errors, input_encoding)
    else:
        return input


def decode(input, encoding='utf-8', errors='strict', detect='utf-8'):
    """Decode any string. Returns a decoded 'str' otherwise the input."""
    if isinstance(input, bytes):
        try:
            r = dec(input, encoding, errors)
        except:
            r = dec(input, det(input)['encoding'], errors)

        if isinstance(r, bytes):
            return decode(r, detect, errors, detect)
        else:
            return r.replace('\ufeff', '', 1)
    elif isinstance(input, str):
        if encoding == Py.Enc.default:
            return input
        else:
            return decode(enc(input, 'latin-1'), encoding, errors, detect)
    else:
        return input
