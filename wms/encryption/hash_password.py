import base64
import hashlib

import bcrypt


def hash_password(password="python", encryption_file=None):
    """Hash password function

    This file helps to hash the password using bcrypt.

    Returns:
        None
    """

    hashed_pw = bcrypt.hashpw(base64.b64encode(hashlib.sha512(password.encode()).digest()), bcrypt.gensalt())
    with open(encryption_file, "w+b") as f:
        f.write(hashed_pw)
