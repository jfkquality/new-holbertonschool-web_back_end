#!/usr/bin/env python3

import bcrypt

# class Auth:
#     """ Auth class """


def _hash_password(password: str) -> str:
    """ hash password """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)
