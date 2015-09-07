#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

from tocoli import Py, PY2
import tocoli.py2.enc as py2enc
import tocoli.py3.enc as py3enc

def encode(input, encoding='utf-8', errors='strict', input_encoding='utf-8'):
    """Encode any string. Returns always a byte string.

    Use this funtion to encode strings you like to write to any kind of output
    (e.g. stdout, file, API, …). This is useful to exchange information in a
    standardized way (the encoding). This function is a universal wrapper for
    the built-in `codecs.encode()` function.

    Examples:
        Default usage::

            >>> encode('café')
            b'caf\xc3\xa9'      # utf-8 encoded byte string

        Transform encoding::

            >>> encode('caf\xe9', 'utf-8', input_encoding='latin-1')
            b'caf\xc3\xa9'      # utf-8 encoded byte string

        Advanced codec support::

            >>> encode('café', 'base64')
            b'Y2Fmw6k=\n'       # base64 encoded byte string
                                # inner encoding is always utf-8

    Args:
        input (str): Any string you like to encode.
            The string can be a byte string or a unicode decoded string. The
            function makes sure to treat the input type in the correct manner.

        encoding (Optional[str]): Output encoding. Defaults to utf-8.
            Defines the encoding for the resulting byte string.

        errors (Optional[str]): Error handling schemes. Defaults to 'strict'
            These string values are predefined:

             'strict' - raise a ValueError error (or a subclass)
             'ignore' - ignore the character and continue with the next
             'replace' - replace with a suitable replacement character;
                        Python will use the official U+FFFD REPLACEMENT
                        CHARACTER for the builtin Unicode codecs on
                        decoding and '?' on encoding.
             'xmlcharrefreplace' - Replace with the appropriate XML
                                   character reference (only for encoding).
             'backslashreplace'  - Replace with backslashed escape sequences
                                   (only for encoding).

        input_encoding (Optional[str]): Given encoding. Defaults to utf-8.
            Set this parameter if your input is not encoded as utf-8.

    Returns:
        str   (python2)
        bytes (python3): Encoded byte string.

    """
    if PY2:
        return py2enc.encode(input, encoding, errors, input_encoding)
    else:
        try:
            return py3enc.encode(input, encoding, errors, input_encoding)
        except:
            raise NotImplementedError(Py.Ver.text + ' is not supported')


def decode(input, encoding='utf-8', errors='strict', detect='utf-8'):
    """Decode any string. Returns always a unicode decoded string.

    Use this function to decode an encoded string. Its recommended to use this
    function as early as possible in your data flow, when you received data
    from an external resource (e.g. stdin, file, API, …). Once decoded you
    have access to the encoded information and can operate on it. This func-
    tion is a universal wrapper for the built-in `codecs.decode()` function.

    Examples:
        Default encoding utf-8::

            >>> decode('caf\xc3\xa9')
            u'café'     # utf-8 decoded string

        Non default encoding::

            >>> decode('caf\xe9', 'latin-1')
            u'café'     # utf-8 decoded string

        Advanced codec support::

            >>> encode('Y2Fmw6k=\n', 'base64')
            u'café'     # utf-8 decoded string

    Args:
        input (str): Any string you like to decode.
            The string can be a byte string or a unicode decoded string. The
            function makes sure to treat the input type in the correct manner.

        encoding (Optional[str]): Input encoding. Defaults to utf-8.
            Defines the encoding of the input.

        errors (Optional[str]): Error handling schemes. Defaults to 'strict'
            These string values are predefined:

             'strict' - raise a ValueError error (or a subclass)
             'ignore' - ignore the character and continue with the next
             'replace' - replace with a suitable replacement character;
                        Python will use the official U+FFFD REPLACEMENT
                        CHARACTER for the builtin Unicode codecs on
                        decoding and '?' on encoding.
             'xmlcharrefreplace' - Replace with the appropriate XML
                                   character reference (only for encoding).
             'backslashreplace'  - Replace with backslashed escape sequences
                                   (only for encoding).

        detect (Optional[str]): Inner encoding. Defaults to utf-8.
            This parameter defines the recursive decoding type (e.g. contains
            a `base64` encoded string inside another encoded string, which might
            be a utf-8 or something else). If the given inner decoding type is
            not correct, then the function tries to detect the encoding auto-
            matically.

    Returns:
        unicode (python2)
        str     (python3): Encoded byte string.

    """
    if PY2:
        return py2enc.decode(input, encoding, errors, detect)
    else:
        try:
            return py3enc.decode(input, encoding)
        except:
            raise NotImplementedError(Py.Ver.text + ' is not supported')
