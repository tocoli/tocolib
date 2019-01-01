#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class Tests(unittest.TestCase):

    def test_CONSTANTS(self):
        from tocoli.regex import ANY, WORD, NOT_WORD, DIGIT, NOT_DIGIT, WHITESPACE, NOT_WHITESPACE

        self.assertEqual(ANY, '.')
        self.assertEqual(WORD, '\\w')
        self.assertEqual(NOT_WORD, '\\W')
        self.assertEqual(DIGIT, '\\d')
        self.assertEqual(NOT_DIGIT, '\\D')
        self.assertEqual(WHITESPACE, '\\s')
        self.assertEqual(NOT_WHITESPACE, '\\S')

        from tocoli.regex import BEGINNING, END, WORD_BOUNDARY, NOT_WORD_BOUNDARY
        self.assertEqual(BEGINNING, '^')
        self.assertEqual(END, '$')
        self.assertEqual(WORD_BOUNDARY, '\\b')
        self.assertEqual(NOT_WORD_BOUNDARY, '\\B')

        from tocoli.regex import Escaped
        self.assertEqual(Escaped.TAB, '\\t')
        self.assertEqual(Escaped.LINE_FEED, '\\n')
        self.assertEqual(Escaped.VERTICAL_TAB, '\\v')
        self.assertEqual(Escaped.FORM_FEED, '\\f')
        self.assertEqual(Escaped.CARRIAGE_RETURN, '\\r')
        self.assertEqual(Escaped.NULL, '\\0')

        from tocoli.regex import PLUS, STAR, OPTIONAL
        self.assertEqual(PLUS, '+')
        self.assertEqual(STAR, '*')
        self.assertEqual(OPTIONAL, '?')

        from tocoli.regex import ALTERNATION
        self.assertEqual(ALTERNATION, '|')

        from tocoli.regex import Substitution
        self.assertEqual(Substitution.MATCH, '$&')
        self.assertEqual(Substitution.BEFORE_MATCH, '$`')
        self.assertEqual(Substitution.AFTER_MATCH, "$'")
        self.assertEqual(Substitution.DOLLAR, '$$')

        from tocoli.regex import Flags
        self.assertEqual(Flags.IGNORE_CASE, 'i')
        self.assertEqual(Flags.GLOBAL_SEARCH, 'g')
        self.assertEqual(Flags.MULTILINE, 'm')

    def test_set(self):
        from tocoli.regex import set

        # not allowed
        self.assertRaises(TypeError, set)

        # simple
        self.assertEqual(set('a'), u'[a]')
        self.assertEqual(set('1'), u'[1]')

        # be set like
        self.assertEqual(set('aa'), u'[a]')

        # sort yourself
        self.assertEqual(set('abc'), u'[abc]')
        self.assertEqual(set('acb'), u'[abc]')
        self.assertEqual(set('bac'), u'[abc]')
        self.assertEqual(set('bca'), u'[abc]')
        self.assertEqual(set('cab'), u'[abc]')
        self.assertEqual(set('cba'), u'[abc]')

        self.assertEqual(set('1a'), u'[1a]')
        self.assertEqual(set('a1'), u'[1a]')

        # handle unicode
        self.assertEqual(set(u'aä'), u'[aä]')
        self.assertEqual(set(u'äa'), u'[aä]')

    def test_negated_set(self):
        from tocoli.regex import negated_set

        # not allowed
        self.assertRaises(TypeError, negated_set)

        # simple
        self.assertEqual(negated_set('a'), u'[^a]')
        self.assertEqual(negated_set('1'), u'[^1]')

        # be set like
        self.assertEqual(negated_set('aa'), u'[^a]')

        # sort yourself
        self.assertEqual(negated_set('abc'), u'[^abc]')
        self.assertEqual(negated_set('acb'), u'[^abc]')
        self.assertEqual(negated_set('bac'), u'[^abc]')
        self.assertEqual(negated_set('bca'), u'[^abc]')
        self.assertEqual(negated_set('cab'), u'[^abc]')
        self.assertEqual(negated_set('cba'), u'[^abc]')

        self.assertEqual(negated_set('1a'), u'[^1a]')
        self.assertEqual(negated_set('a1'), u'[^1a]')

        # handle unicode
        self.assertEqual(negated_set(u'aä'), u'[^aä]')
        self.assertEqual(negated_set(u'äa'), u'[^aä]')

    def test_range(self):
        from tocoli.regex import range

        self.assertEqual(range('0', '9'), u'0-9')

        self.assertEqual(range('a', 'z'), u'a-z')
        self.assertEqual(range('A', 'Z'), u'A-Z')
        self.assertEqual(range('a', 'Z'), u'a-zA-Z')

        self.assertEqual(range(u'ä', u'ö'), u'ä-ö')
        self.assertEqual(range(u'Ä', u'Ö'), u'Ä-Ö')
        self.assertEqual(range(u'ä', u'Ö'), u'ä-öÄ-Ö')

    def test_escape_octal(self):
        from tocoli.regex import escape_octal

        self.assertRaises(TypeError, escape_octal, 8.8)
        self.assertRaises(ValueError, escape_octal, 512)
        self.assertRaises(ValueError, escape_octal, '888')

        self.assertEqual(escape_octal('0'), u'\\000')
        self.assertEqual(escape_octal('7'), u'\\007')

        self.assertEqual(escape_octal('00'), u'\\000')
        self.assertEqual(escape_octal('77'), u'\\077')

        self.assertEqual(escape_octal('000'), u'\\000')
        self.assertEqual(escape_octal('777'), u'\\777')

        self.assertEqual(escape_octal(0), u'\\000')
        self.assertEqual(escape_octal(1), u'\\001')
        self.assertEqual(escape_octal(8), u'\\010')
        self.assertEqual(escape_octal(64), u'\\100')
        self.assertEqual(escape_octal(511), u'\\777')

    def test_escape_hexadecimal(self):
        from tocoli.regex import escape_hexadecimal

        self.assertRaises(TypeError, escape_hexadecimal, 8.8)
        self.assertRaises(ValueError, escape_hexadecimal, 256)
        self.assertRaises(ValueError, escape_hexadecimal, 'GG')

        self.assertEqual(escape_hexadecimal('0'), u'\\x00')
        self.assertEqual(escape_hexadecimal('1'), u'\\x01')
        self.assertEqual(escape_hexadecimal('f'), u'\\x0F')
        self.assertEqual(escape_hexadecimal('F'), u'\\x0F')

        self.assertEqual(escape_hexadecimal('00'), u'\\x00')
        self.assertEqual(escape_hexadecimal('01'), u'\\x01')
        self.assertEqual(escape_hexadecimal('10'), u'\\x10')
        self.assertEqual(escape_hexadecimal('ff'), u'\\xFF')
        self.assertEqual(escape_hexadecimal('FF'), u'\\xFF')

        self.assertEqual(escape_hexadecimal(0), u'\\x00')
        self.assertEqual(escape_hexadecimal(1), u'\\x01')
        self.assertEqual(escape_hexadecimal(16), u'\\x10')
        self.assertEqual(escape_hexadecimal(255), u'\\xFF')

    def test_escape_unicode(self):
        from tocoli.regex import escape_unicode

        self.assertRaises(TypeError, escape_unicode, 8.8)
        self.assertRaises(ValueError, escape_unicode, 65536)
        self.assertRaises(ValueError, escape_unicode, 'GGGG')

        self.assertEqual(escape_unicode('0'), u'\\u0000')
        self.assertEqual(escape_unicode('1'), u'\\u0001')
        self.assertEqual(escape_unicode('f'), u'\\u000F')
        self.assertEqual(escape_unicode('F'), u'\\u000F')

        self.assertEqual(escape_unicode('0000'), u'\\u0000')
        self.assertEqual(escape_unicode('0001'), u'\\u0001')
        self.assertEqual(escape_unicode('0010'), u'\\u0010')
        self.assertEqual(escape_unicode('0100'), u'\\u0100')
        self.assertEqual(escape_unicode('1000'), u'\\u1000')
        self.assertEqual(escape_unicode('ffff'), u'\\uFFFF')
        self.assertEqual(escape_unicode('FFFF'), u'\\uFFFF')

        self.assertEqual(escape_unicode(0), u'\\u0000')
        self.assertEqual(escape_unicode(1), u'\\u0001')
        self.assertEqual(escape_unicode(16), u'\\u0010')
        self.assertEqual(escape_unicode(256), u'\\u0100')
        self.assertEqual(escape_unicode(4096), u'\\u1000')
        self.assertEqual(escape_unicode(65535), u'\\uFFFF')


    def test_escape_control_char(self):
        from tocoli.regex import escape_control_char

        self.assertRaises(ValueError, escape_control_char, '0')
        self.assertRaises(ValueError, escape_control_char, 0)

        self.assertEqual(escape_control_char(65), '\\cA')
        self.assertEqual(escape_control_char(90), '\\cZ')

        self.assertEqual(escape_control_char('a'), '\\cA')
        self.assertEqual(escape_control_char('z'), '\\cZ')

        self.assertEqual(escape_control_char('A'), '\\cA')
        self.assertEqual(escape_control_char('Z'), '\\cZ')

    def test_group_capturing(self):
        from tocoli.regex import group_capturing

        self.assertEqual(group_capturing(''), u'()')

        self.assertEqual(group_capturing('a'), u'(a)')
        self.assertEqual(group_capturing('A'), u'(A)')

        self.assertEqual(group_capturing(1), u'(1)')

        self.assertEqual(group_capturing(u'ä'), u'(ä)')

    def test_group_non_capturing(self):
        from tocoli.regex import group_non_capturing

        self.assertEqual(group_non_capturing(''), u'(?:)')

        self.assertEqual(group_non_capturing('a'), u'(?:a)')
        self.assertEqual(group_non_capturing('A'), u'(?:A)')

        self.assertEqual(group_non_capturing(1), u'(?:1)')

        self.assertEqual(group_non_capturing(u'ä'), u'(?:ä)')

    def test_group(self):
        from tocoli.regex import group

        # capturing
        self.assertEqual(group(''), u'()')

        self.assertEqual(group('a'), u'(a)')
        self.assertEqual(group('A'), u'(A)')

        self.assertEqual(group(1), u'(1)')

        self.assertEqual(group(u'ä'), u'(ä)')

        # non capturing
        self.assertEqual(group('', False), u'(?:)')

        self.assertEqual(group('a', False), u'(?:a)')
        self.assertEqual(group('A', False), u'(?:A)')

        self.assertEqual(group(1, False), u'(?:1)')

        self.assertEqual(group(u'ä', False), u'(?:ä)')

    def test_backreference(self):
        from tocoli.regex import backreference

        self.assertRaises(TypeError, backreference, 8.8)
        self.assertRaises(TypeError, backreference, '')
        self.assertRaises(TypeError, backreference, u'')
        self.assertRaises(ValueError, backreference, -1)

        self.assertEqual(backreference(0), u'\\0')
        self.assertEqual(backreference(1), u'\\1')
        self.assertEqual(backreference(10), u'\\10')

    def test_lookahead_positive(self):
        from tocoli.regex import lookahead_positive

        self.assertEqual(lookahead_positive('', ''), u'(?=)')

        self.assertEqual(lookahead_positive('\\w', 'a'), u'\\w(?=a)')
        self.assertEqual(lookahead_positive('\\w', 'A'), u'\\w(?=A)')

        self.assertEqual(lookahead_positive('\\d', 1), u'\\d(?=1)')

        self.assertEqual(lookahead_positive('\\w', u'ä'), u'\\w(?=ä)')

    def test_lookahead_negative(self):
        from tocoli.regex import lookahead_negative

        self.assertEqual(lookahead_negative('', ''), u'(?!)')

        self.assertEqual(lookahead_negative('\\w', 'a'), u'\\w(?!a)')
        self.assertEqual(lookahead_negative('\\w', 'A'), u'\\w(?!A)')

        self.assertEqual(lookahead_negative('\\d', 1), u'\\d(?!1)')

        self.assertEqual(lookahead_negative('\\w', u'ä'), u'\\w(?!ä)')

    def test_lookahead(self):
        from tocoli.regex import lookahead

        # positive
        self.assertEqual(lookahead('', ''), u'(?=)')

        self.assertEqual(lookahead('\\w', 'a'), u'\\w(?=a)')
        self.assertEqual(lookahead('\\w', 'A'), u'\\w(?=A)')

        self.assertEqual(lookahead('\\d', 1), u'\\d(?=1)')

        self.assertEqual(lookahead('\\w', u'ä'), u'\\w(?=ä)')

        # negative
        self.assertEqual(lookahead('', '', False), u'(?!)')

        self.assertEqual(lookahead('\\w', 'a', False), u'\\w(?!a)')
        self.assertEqual(lookahead('\\w', 'A', False), u'\\w(?!A)')

        self.assertEqual(lookahead('\\d', 1, False), u'\\d(?!1)')

        self.assertEqual(lookahead('\\w', u'ä', False), u'\\w(?!ä)')

    def test_lookbehind_positive(self):
        from tocoli.regex import lookbehind_positive

        self.assertEqual(lookbehind_positive('', ''), u'(?<=)')

        self.assertEqual(lookbehind_positive('\\w', 'a'), u'\\w(?<=a)')
        self.assertEqual(lookbehind_positive('\\w', 'A'), u'\\w(?<=A)')

        self.assertEqual(lookbehind_positive('\\d', 1), u'\\d(?<=1)')

        self.assertEqual(lookbehind_positive('\\w', u'ä'), u'\\w(?<=ä)')

    def test_lookbehind_negative(self):
        from tocoli.regex import lookbehind_negative

        self.assertEqual(lookbehind_negative('', ''), u'(?<!)')

        self.assertEqual(lookbehind_negative('\\w', 'a'), u'\\w(?<!a)')
        self.assertEqual(lookbehind_negative('\\w', 'A'), u'\\w(?<!A)')

        self.assertEqual(lookbehind_negative('\\d', 1), u'\\d(?<!1)')

        self.assertEqual(lookbehind_negative('\\w', u'ä'), u'\\w(?<!ä)')

    def test_lookbehind(self):
        from tocoli.regex import lookbehind

        # positive
        self.assertEqual(lookbehind('', ''), u'(?<=)')

        self.assertEqual(lookbehind('\\w', 'a'), u'\\w(?<=a)')
        self.assertEqual(lookbehind('\\w', 'A'), u'\\w(?<=A)')

        self.assertEqual(lookbehind('\\d', 1), u'\\d(?<=1)')

        self.assertEqual(lookbehind('\\w', u'ä'), u'\\w(?<=ä)')

        # negative
        self.assertEqual(lookbehind('', '', False), u'(?<!)')

        self.assertEqual(lookbehind('\\w', 'a', False), u'\\w(?<!a)')
        self.assertEqual(lookbehind('\\w', 'A', False), u'\\w(?<!A)')

        self.assertEqual(lookbehind('\\d', 1, False), u'\\d(?<!1)')

        self.assertEqual(lookbehind('\\w', u'ä', False), u'\\w(?<!ä)')

    def test_plus(self):
        from tocoli.regex import plus

        self.assertEqual(plus(''), u'+')
        self.assertEqual(plus('a'), u'a+')
        self.assertEqual(plus('A'), u'A+')
        self.assertEqual(plus(u'ä'), u'ä+')
        self.assertEqual(plus(u'Ä'), u'Ä+')
        self.assertEqual(plus('1'), u'1+')
        self.assertEqual(plus(1), u'1+')

    def test_star(self):
        from tocoli.regex import star

        self.assertEqual(star(''), u'*')
        self.assertEqual(star('a'), u'a*')
        self.assertEqual(star('A'), u'A*')
        self.assertEqual(star(u'ä'), u'ä*')
        self.assertEqual(star(u'Ä'), u'Ä*')
        self.assertEqual(star('1'), u'1*')
        self.assertEqual(star(1), u'1*')

    def test_optional(self):
        from tocoli.regex import optional

        self.assertEqual(optional(''), u'?')
        self.assertEqual(optional('a'), u'a?')
        self.assertEqual(optional('A'), u'A?')
        self.assertEqual(optional(u'ä'), u'ä?')
        self.assertEqual(optional(u'Ä'), u'Ä?')
        self.assertEqual(optional('1'), u'1?')
        self.assertEqual(optional(1), u'1?')

    def test_quantifier(self):
        from tocoli.regex import quantify

        self.assertRaises(ValueError, quantify, '', '')
        self.assertRaises(ValueError, quantify, '', 1, 'a')

        self.assertEqual(quantify('', 0), u'{0,}')
        self.assertEqual(quantify('', 1), u'{1,}')
        self.assertEqual(quantify('', 1, ''), u'{1,}')
        self.assertEqual(quantify('', 1, None), u'{1,}')
        self.assertEqual(quantify('', 1, False), u'{1,}')

        self.assertEqual(quantify('', 0, 1), u'{0,1}')
        self.assertEqual(quantify('', 0, 100), u'{0,100}')

        self.assertEqual(quantify('', '0', '1'), u'{0,1}')
        self.assertEqual(quantify('', '0', '100'), u'{0,100}')

        self.assertEqual(quantify(u'', u'0', u'1'), u'{0,1}')
        self.assertEqual(quantify(u'', u'0', u'100'), u'{0,100}')

        self.assertEqual(quantify(u'ä', u'0', u'100'), u'ä{0,100}')

    def test_quantify_lazy(self):
        from tocoli.regex import quantify_lazy

        self.assertRaises(ValueError, quantify_lazy, '', '')
        self.assertRaises(ValueError, quantify_lazy, '', 1, 'a')

        self.assertEqual(quantify_lazy('', 0), u'{0,}?')
        self.assertEqual(quantify_lazy('', 1), u'{1,}?')
        self.assertEqual(quantify_lazy('', 1, ''), u'{1,}?')
        self.assertEqual(quantify_lazy('', 1, None), u'{1,}?')
        self.assertEqual(quantify_lazy('', 1, False), u'{1,}?')

        self.assertEqual(quantify_lazy('', 0, 1), u'{0,1}?')
        self.assertEqual(quantify_lazy('', 0, 100), u'{0,100}?')

        self.assertEqual(quantify_lazy('', '0', '1'), u'{0,1}?')
        self.assertEqual(quantify_lazy('', '0', '100'), u'{0,100}?')

        self.assertEqual(quantify_lazy(u'', u'0', u'1'), u'{0,1}?')
        self.assertEqual(quantify_lazy(u'', u'0', u'100'), u'{0,100}?')

        self.assertEqual(quantify_lazy(u'ä', u'0', u'100'), u'ä{0,100}?')

    def test_lazy(self):
        from tocoli.regex import lazy, star, plus, optional

        self.assertEqual(lazy(star('')), u'*?')
        self.assertEqual(lazy(plus('')), u'+?')
        self.assertEqual(lazy(optional('')), u'??')

        self.assertEqual(lazy(star('a')), u'a*?')
        self.assertEqual(lazy(plus('a')), u'a+?')
        self.assertEqual(lazy(optional('a')), u'a??')

    def test_alternate(self):
        from tocoli.regex import alternate

        self.assertEqual(alternate('', ''), u'|')
        self.assertEqual(alternate('a', 'b'), u'a|b')
        self.assertEqual(alternate(u'ä', u'ü'), u'ä|ü')

    # @unittest.skip("skip this test")
    def test_generate(self):
        from tocoli.regex import generate

        self.assertRaises(TypeError, generate, None)

        #
        # 0 char
        #

        res = generate('')
        self.assertEqual(res, '')

        #
        # 1 char
        #

        res = generate('a')
        self.assertEqual(res, 'a')

        res = generate('a', start=True)
        self.assertEqual(res, '^a')

        res = generate('a', end=True)
        self.assertEqual(res, 'a$')

        res = generate('a', match='.')
        self.assertEqual(res, 'a.{0,}?')

        res = generate('a', setLike=True)
        self.assertEqual(res, 'a')

        res = generate('a', start=True, match='.')
        self.assertEqual(res, '^a.{0,}?')

        res = generate('a', end=True, match='.')
        self.assertEqual(res, 'a.{0,}?$')

        res = generate('a', match='.', setLike=True)
        self.assertEqual(res, 'a.{0,}?')

        res = generate('a', start=True, match='.', setLike=True)
        self.assertEqual(res, '^a.{0,}?')

        res = generate('a', end=True, match='.', setLike=True)
        self.assertEqual(res, 'a.{0,}?$')

        res = generate('a', start=True, end=True, match='.', setLike=True)
        self.assertEqual(res, '^a.{0,}?$')

        #
        # 2 chars
        #

        res = generate('ab', start=True)
        self.assertEqual(res, '^ab')

        res = generate('ab', end=True)
        self.assertEqual(res, 'ab$')

        res = generate('ab', match='.')
        self.assertEqual(res, 'a.{0,}?b.{0,}?')

        res = generate('ab', setLike=True)
        self.assertEqual(res, '(a|b)(a|b)')

        res = generate('ab', start=True, match='.')
        self.assertEqual(res, '^a.{0,}?b.{0,}?')

        res = generate('ab', end=True, match='.')
        self.assertEqual(res, 'a.{0,}?b$')

        res = generate('ab', match='.', setLike=True)
        self.assertEqual(res, '(a|b).{0,}?(a|b).{0,}?')

        res = generate('ab', start=True, match='.', setLike=True)
        self.assertEqual(res, '^a.{0,}?b.{0,}?')

        res = generate('ab', end=True, match='.', setLike=True)
        self.assertEqual(res, 'a.{0,}?b$')

        res = generate('ab', start=True, end=True, match='.', setLike=True)
        self.assertEqual(res, '^a.{0,}?b$')

        #
        # 3 chars
        #

        res = generate('abc', start=True)
        self.assertEqual(res, '^abc')

        res = generate('abc', end=True)
        self.assertEqual(res, 'abc$')

        res = generate('abc', match='.')
        self.assertEqual(res, 'a.{0,}?b.{0,}?c.{0,}?')

        res = generate('abc', setLike=True)
        self.assertEqual(res, '(a|b|c)(a|b|c)(a|b|c)')

        res = generate('abc', start=True, match='.')
        self.assertEqual(res, '^a.{0,}?b.{0,}?c.{0,}?')

        res = generate('abc', end=True, match='.')
        self.assertEqual(res, 'a.{0,}?b.{0,}?c$')

        res = generate('abc', match='.', setLike=True)
        self.assertEqual(res, '(a|b|c).{0,}?(a|b|c).{0,}?(a|b|c).{0,}?')

        res = generate('abc', start=True, match='.', setLike=True)
        self.assertEqual(res, '^a.{0,}?(b|c).{0,}?(b|c).{0,}?')

        res = generate('abc', end=True, match='.', setLike=True)
        self.assertEqual(res, '(a|b).{0,}?(a|b).{0,}?c$')

        res = generate('abc', start=True, end=True, match='.', setLike=True)
        self.assertEqual(res, '^a.{0,}?b.{0,}?c$')

        #
        # 4 chars
        #

        res = generate('abcd', start=True)
        self.assertEqual(res, '^abcd')

        res = generate('abcd', end=True)
        self.assertEqual(res, 'abcd$')

        res = generate('abcd', match='.')
        self.assertEqual(res, 'a.{0,}?b.{0,}?c.{0,}?d.{0,}?')

        res = generate('abcd', setLike=True)
        self.assertEqual(res, '(a|b|c|d)(a|b|c|d)(a|b|c|d)(a|b|c|d)')

        res = generate('abcd', start=True, match='.')
        self.assertEqual(res, '^a.{0,}?b.{0,}?c.{0,}?d.{0,}?')

        res = generate('abcd', end=True, match='.')
        self.assertEqual(res, 'a.{0,}?b.{0,}?c.{0,}?d$')

        res = generate('abcd', match='.', setLike=True)
        self.assertEqual(res, '(a|b|c|d).{0,}?(a|b|c|d).{0,}?(a|b|c|d).{0,}?(a|b|c|d).{0,}?')

        res = generate('abcd', match='\S', setLike=True)
        self.assertEqual(res, '(a|b|c|d)\S{0,}?(a|b|c|d)\S{0,}?(a|b|c|d)\S{0,}?(a|b|c|d)\S{0,}?')

        res = generate('abcd', start=True, match='.', setLike=True)
        self.assertEqual(res, '^a.{0,}?(b|c|d).{0,}?(b|c|d).{0,}?(b|c|d).{0,}?')

        res = generate('abcd', end=True, match='.', setLike=True)
        self.assertEqual(res, '(a|b|c).{0,}?(a|b|c).{0,}?(a|b|c).{0,}?d$')

        res = generate('abcd', start=True, end=True, match='.', setLike=True)
        self.assertEqual(res, '^a.{0,}?(b|c).{0,}?(b|c).{0,}?d$')


class TestRe(unittest.TestCase):

    # @unittest.skip("skip this test")
    def test_generate(self):
        import re
        from tocoli.regex import Re, ANY, BEGINNING
        # from tocoli import regex

        r = re.compile(Re('[ab]'))
        m = r.match('a')
        self.assertIsNotNone(m)
        self.assertEqual(m.span(), (0, 1))
        m = r.match('b')
        self.assertIsNotNone(m)
        self.assertEqual(m.span(), (0, 1))
        m = r.match('c')
        self.assertIsNone(m)

        e = Re('a') | Re('b')
        self.assertEqual(e, u'a|b')

        e = Re('a') & Re('b')
        self.assertEqual(e, u'ab')

        e = Re('a') + Re('b')
        self.assertEqual(e, u'ab')

        expr = (Re('hello') | Re('bello')).group().quantify(0,1).lazy().add("world")
        self.assertEqual(expr, u'(hello|bello){0,1}?world')

        expr = Re('h').add_set('ae').add('llo world')
        self.assertEqual(expr, u'h[ae]llo world')

        expr = Re(ANY).lookahead('\\\\', False).add('-' + ANY).lookahead('\\\\', False).group()
        self.assertEqual(expr, u'(.(?!\\\\)-.(?!\\\\))')

        expr = BEGINNING + Re(r'\\-\\a-zA-Zbcd\\\|').set()
        self.assertEqual(expr, r'^[A-Z\\\\-\\\|a-z]')


if __name__ == '__main__':
    unittest.main()
