#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tocoli.filter import clean

class strip:
    from tocoli.map import map_to_non_accented_characters as accents
    accents = staticmethod(accents)
