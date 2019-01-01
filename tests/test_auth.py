#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class Tests(unittest.TestCase):

    # @unittest.skip("skip this test")
    def test_generate_salt(self):
        import string
        from tocoli.auth import generate_salt, SALT_RANGE

        salt = generate_salt()
        self.assertTrue(all(s in SALT_RANGE for s in salt))
        self.assertEqual(len(salt), 10)

        salt = generate_salt(15)
        self.assertTrue(all(s in SALT_RANGE for s in salt))
        self.assertEqual(len(salt), 15)

        salt = generate_salt(chars=string.ascii_lowercase)
        self.assertTrue(all(s in string.ascii_lowercase for s in salt))
        self.assertEqual(len(salt), 10)


    def test_encrypt_password_and_verify_password(self):
        from tocoli.auth import encrypt_password, verify_password

        hash = encrypt_password('secret', rounds=1001)
        elems = [h for h in hash.split('$') if len(h) > 0]
        self.assertEqual(elems[0], '5')
        self.assertEqual(elems[1], 'rounds=1001')
        self.assertEqual(len(elems[2]), 16)
        self.assertEqual(len(elems[3]), 43)
        self.assertTrue(verify_password(hash, 'secret'))

    def test_encrypt_token_and_verify_token(self):
        from tocoli.auth import encrypt_token, verify_token

        token = encrypt_token(u'Alice', u'secret', expiration=-1)
        self.assertEqual(verify_token(token, u'secret'), None)

        token = encrypt_token(u'Alice', u'secret') + 'modified'.encode('ascii')
        self.assertEqual(verify_token(token, u'secret'), None)

        token = encrypt_token(u'Alice', u'secret')
        self.assertEqual(verify_token(token, u'secret'), u'Alice')

    def test_encrypt_api_key_and_verify_api_key(self):
        from tocoli.auth import encrypt_api_key, verify_api_key

        api_key = encrypt_api_key(u'Alice', u'secret') + 'modified'.encode('ascii')
        self.assertEqual(verify_api_key(api_key, u'secret'), None)

        api_key = encrypt_api_key(u'Alice', u'secret')
        self.assertEqual(verify_api_key(api_key, u'secret'), u'Alice')




if __name__ == '__main__':
    unittest.main()
