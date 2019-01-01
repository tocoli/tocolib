#!/usr/bin/env python
# -*- coding: utf-8 -*-


STRICT = 'strict'
WIDE = 'wide'

def lookup(word, dictionary):

    word = word.lower()
    res = []
    pair = False

    for i, c in enumerate(word):
        if pair:
            pair = False
        else:
            try:
                try:
                    nextC = word[i + 1]
                except IndexError:
                    alt = dictionary[c]
                else:
                    try:
                        alt = dictionary[c + nextC]
                    except KeyError:
                        alt = dictionary[c]
                    else:
                        pair = True
            except KeyError:
                alt = c
            finally:
                res.append(alt)

    return res

class Dictionary:
    latin = {
        STRICT : {
            u'a': u'a|á|ä',
            u'as': u'as|ás|a|á|s',
            u'á': u'a|á|ä',
            u'ä': u'a|á|ä',
            u'b': u'b|v',
            u'c': u'cc|c|z',
            u'cc': u'cc|ck|c|k',
            u'e': u'e|é',
            u'é': u'e|é',
            u'es': u'es|e|s',
            u'g': u'g|j',
            u'i': u'i|í|y',
            u'í': u'i|í|y',
            u'j': u'j|g|y|c|h',
            u'k': u'k|c|q',
            u'l': u'll|l',
            u'll': u'll|l|j|y',
            u'n': u'n|nn|ñ',
            u'nn': u'nn|n|ñ',
            u'ñ': u'n|ñ',
            u'o': u'o|ó|ö',
            u'os': u'os|o|s|a',
            u'ó': u'o|ó|ö',
            u'ö': u'o|ó|ö',
            u'r': u'rr|r',
            u'rr': u'rr|r',
            u's': u'ss|s|z|c',
            u't': u'tt|t',
            u'tt': u'tt|t',
            u'u': u'u|ú|ue|üe|ü',
            u'ú': u'u|ú|ue|üe|ü',
            u'ü': u'u|ú|ue|üe|ü',
            u'v': u'v|b',
            u'y': u'y|ll|i',
            u'z': u'z|c|s|ss'
        },
        WIDE : {
            u'a': u'a|á|ä|o|ó|e',
            u'á': u'a|á|ä|o|ó',
            u'ä': u'a|á|ä|o|ó',
            u'ai': u'ai|i|y',
            u'ay': u'ay|i|y',
            u'b': u'b|v|w',
            u'c': u'cc|c|k|s|z|q|x|h',
            u'cc': u'cc|c|k|s|z|q|x|h',
            u'd': u'd|t',
            u'e': u'e|é|i',
            u'é': u'e|é|i',
            u'es': u'es|és|e|s|al',
            u'g': u'g|j|h|c|q',
            u'h': u'h|g|x',
            u'i': u'i|í|y|e|l',
            u'í': u'i|í|y|e|l',
            u'ie': u'ie|íe|ié|i|e|le',
            u'is': u'is|ís|i|í|s|ls',
            u'j': u'j|g|y|c|h',
            u'ji': u'ji|jí|hi|hí|xi|xí|y|i|í',
            u'k': u'ca|k|c|q',
            u'l': u'll|l|j|i',
            u'll': u'll|l|j|y|ii|i',
            u'm': u'm|n',
            u'n': u'nn|n|ñ|m',
            u'nn': u'nn|n|ñ|m',
            u'ñ': u'nn|n|ñ|m',
            u'o': u'o|ó|ö|u|a|á',
            u'ou': u'ou|óu|oú|o|u',
            u'os': u'os|ós|o|ó|s|a',
            u'ó': u'o|ó|ö|u|a|á',
            u'ö': u'o|ó|ö|u|a|á',
            u'q': u'q|k|c',
            u'r': u'r|rr',
            u'rr': u'rr|r',
            u's': u'ss|c|s|z|ß|th',
            u'sc': u'ssc|sch|sc|sz|c|s',
            u'sch': u'ssh|sch|sh|ch|sc|h|s',
            u'se': u'sse|ssé|se|sé|e|s',
            u'sh': u'ssh|sch|sh|ch|sc|h|s|ge',
            u'ss': u'ss|s|ß',
            u'sz': u'sz|s|z',
            u't': u'tt|d|t',
            u'tt': u'tt|d|t',
            u'u': u'ue|üe|u|ú|ü|v|w|a',
            u'ú': u'ue|üe|u|ú|ü|v|w|a',
            u'ü': u'ue|üe|u|ú|ü|v|w|a',
            u'v': u'v|b|w',
            u'w': u'w|v|b|u',
            u'x': u'cc|ch|ck|ks|c|j|s|x|z',
            u'y': u'y|ll|i|j',
            u'yi': u'yi|hi|i|y|ji|xi',
            u'z': u'z|c|s'
            }
        }
