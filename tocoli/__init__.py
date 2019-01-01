#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" The tocolib is a multipurpose utility library. """

import sys
import locale
import codecs
from six import *

class Py:

    class Ver:
        major, minor, micro, releaselevel, serial = sys.version_info
        text = sys.version
        hex = sys.hexversion

    class Enc:
        default = 'utf-8'
        preferred = locale.getpreferredencoding().lower()

    @staticmethod
    def std(io=sys.stdout, encoding=Enc.preferred):
        if (io.encoding is None):
            if Py.Ver.major == 2:
                if Py.Ver.minor < 6:
                    raise NotImplementedError("Not implemented for Python " + Py.Ver.text)
                else:
                    return codecs.getwriter(encoding)(io)
            elif Py.Ver.major == 3:
                if Py.Ver.minor < 1:
                    return codecs.getwriter(encoding)(io)
                else:
                    return codecs.getwriter(encoding)(io.detach())
            else:
                return codecs.getwriter(encoding)(io.detach())
        else:
            return io
