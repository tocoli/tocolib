#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @copyright: © 2015 Sebastian Wiesendahl. All rights reserved.
# @author: Sebastian Wiesendahl <sebastian@wiesendahl.de>

import string
import random
from itsdangerous import TimedJSONWebSignatureSerializer as TimedSerializer, SignatureExpired
from itsdangerous import JSONWebSignatureSerializer as Serializer, BadSignature
from passlib.hash import sha256_crypt

SALT_RANGE = string.ascii_uppercase + string.digits + string.ascii_lowercase

def generate_salt(length=10, chars=SALT_RANGE):
    '''Generates a salt. Defaults to a random salt from [A-Z0-9a-z].'''
    r = random.SystemRandom()
    return u''.join(r.choice(chars) for _ in range(length))


def encrypt_password(password, rounds=100001):
    '''Encrypts a password as hash.'''
    return sha256_crypt.encrypt(password, rounds=rounds)


def verify_password(hash, password):
    '''Verifies a password hash. Returns True on success else False'''
    return sha256_crypt.verify(password, hash)


def encrypt_token(user_id, secret_key, expiration=1800):
    '''Encrypts a user id into a timed token. Default expiration time is 30 minutes.'''
    ts = TimedSerializer(secret_key, expires_in=expiration)
    return ts.dumps({ 'id': user_id })


def verify_token(token, secret_key):
    '''Verifies a given token. Returns the decoded user id or None.'''
    ts = TimedSerializer(secret_key)
    try:
        data = ts.loads(token)
    except SignatureExpired:
        return None # valid token, but expired
    except BadSignature:
        return None # invalid token

    return data['id'] if 'id' in data else None


def encrypt_api_key(user_id, secret_key):
    '''Encrypts a user id into an api key (token). The generated api key has no expiration time.'''
    s = Serializer(secret_key)
    return s.dumps({'id': user_id, 'salt': generate_salt()})


def verify_api_key(api_key, secret_key):
    '''Verifies a given api key (token). Returns the decoded user id or None.'''
    s = Serializer(secret_key)
    try:
        data = s.loads(api_key)
    except BadSignature:
        return None # invalid token

    return data['id'] if 'id' in data else None
