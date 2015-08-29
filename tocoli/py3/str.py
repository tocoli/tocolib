#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>


def decode(value, encoding='utf-8'):
    if isinstance(value, bytes):
        return str(value, encoding)
    elif isinstance(value, str):
        return value.encode(encoding).decode(encoding)
    else:
        return value


def encode(value, encoding='utf-8'):
    if isinstance(value, bytes):
        return value.decode(encoding).encode(encoding)
    elif isinstance(value, str):
        return value.encode(encoding)
    else:
        return value
