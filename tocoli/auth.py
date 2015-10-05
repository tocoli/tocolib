#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

from itsdangerous import TimedJSONWebSignatureSerializer as TimedSerializer, SignatureExpired
from itsdangerous import JSONWebSignatureSerializer as Serializer, BadSignature
from passlib.hash import sha256_crypt
import string
import random


def generate_salt(secret_key=None, length=10, chars=string.ascii_lowercase + string.digits):
    '''Generates a salt. Defaults to a random salt from [a-z0-9].'''
    salt = ''
    if secret_key is None:
        salt = ''.join(random.SystemRandom().choice(chars) for _ in range(length))
    else:
        for i in range(length):
            try:
                salt += secret_key[i]
            except:
                salt += '*'
    return salt


class PasswordHandler:
    '''Handle passwords'''

    @staticmethod
    def encrypt(password, rounds=4321):
        '''Encrypts a password as sha256 hash'''
        return sha256_crypt.encrypt(password, rounds=rounds)

    @staticmethod
    def verify(hash, password):
        '''Verifies a password hash. Returns True on success else False'''
        return sha256_crypt.verify(password, hash)


class TokenHandler:
    '''Handle tokens'''

    def __init__(self, secret_key):
        self.secret_key = secret_key

    def encrypt(self, id, expiration=1800):
        '''Encrypts a user id into a timed token. Default expiration time is 30 minutes.'''
        ts = TimedSerializer(self.secret_key, expires_in=expiration)
        return ts.dumps({ 'id': id })

    def verify(self, token):
        '''Verifies a given token. Returns the decoded user id or None.'''
        ts = TimedSerializer(self.secret_key)
        try:
            data = ts.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token

        return data['id'] if 'id' in data else None


class ApiKeyHandler:
    '''Handle api keys'''

    def __init__(self, secret_key):
        self.secret_key = secret_key

    def encrypt(self, id):
        '''Encrypts a user id into an api key (token). The generated api key has no expiration time.'''
        s = Serializer(self.secret_key)
        return s.dumps({'id': id, 'salt': generate_salt()})

    def verify(self, token):
        '''Verifies a given api key (token). Returns the decoded user id or None.'''
        s = Serializer(self.secret_key)
        try:
            data = s.loads(token)
        except BadSignature:
            return None # invalid token

        return data['id'] if 'id' in data else None
