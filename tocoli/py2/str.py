#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

INTERN = 'utf-8'

def encode(input, enc_out='utf-8', enc_in='utf-8'):
    if isinstance(input, str):
        if enc_in == INTERN:
            try:
                return input.decode(enc_in).encode(enc_out)
            except Exception:
                return input.encode(enc_out)
        else:
            try:
                return input.decode(enc_in).decode(INTERN).encode(enc_out)
            except:
                return input.decode(enc_in).encode(enc_out)
    elif isinstance(input, unicode):
        if enc_in == INTERN:
            try:
                return input.encode(enc_out)
            except Exception:
                return input.encode(INTERN).encode(enc_out)
        else:
            try:
                return input.decode(enc_in).decode(INTERN).encode(enc_out)
            except:
                return input.encode('latin-1').decode(enc_in).encode(enc_out)
    else:
        return input


def decode(input, enc_in='utf-8', enc_out='utf-8'):
    if isinstance(input, str):
        if enc_in == enc_out:
            return input.decode(enc_out)
        else:
            input = input.decode(enc_in)
            try:
                if enc_out == INTERN:
                    return input.encode(enc_out).decode(enc_out)
                else:
                    return input.encode(enc_out)
            except:
                try:
                    if enc_out == INTERN:
                        return input.decode(enc_out)
                    else:
                        return input.encode(INTERN).encode(enc_out)
                except:
                    return input.decode(INTERN).encode(enc_out)

    elif isinstance(input, unicode):
        if enc_in == enc_out:
            return input
        else:
            return decode(input.encode('latin-1'), enc_in=enc_in, enc_out=enc_out)
    else:
        return input
