#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import re
import unicodedata


def clean(str, include='', alpha='a-zA-Z', numeric='0-9'):
    """Filter unwanted characters. Returns the filtered string.

        Examples:

            >>> clean('1.20€')
            '120'

            >>> clean('1.20€', '.')
            '1.20'

            >>> clean('1.20€', '.€')
            '1.20€'

            >>> clean('Hello', alpha='a-z')
            'ello'

        Args:
            str (str): input string
            include (str): Regular-expression raw string. Defaults to ''.
                This parameter defines which additional characters to include
                to the result.
            alpha (str): Regular-expression raw string. Defaults to 'a-zA-Z'.
                This parameter defines which alpha characters should be in the
                result.
            numeric (str): Regular-expression raw string. Defaults to '0-9'.
                This parameter defines which numeric characters should be in
                the result.

        Returns:
            str: string which only contains accepted characters.

    """
    return re.sub('[^{}{}{}]+'.format(alpha, numeric, include), '', str)


def strip_accents(str):
   return ''.join(c for c in unicodedata.normalize('NFD', str) if unicodedata.category(c) != 'Mn')


def count_equal_chars(str1, str2):
    return len(set(str1) & set(str2))
