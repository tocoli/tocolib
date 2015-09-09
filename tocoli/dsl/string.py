#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>


from tocoli.filter import clean

class strip:
    from tocoli.map import map_to_non_accented_characters as accents
    accents = staticmethod(accents)
