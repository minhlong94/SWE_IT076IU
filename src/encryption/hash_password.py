import base64
import hashlib
import bcrypt


def hash_password():
    """Hash password function

    This file helps to hash the password using bcrypt.

    Returns:
        None
    """
    password = b"python"
    hashed_pw = bcrypt.hashpw(
        base64.b64encode(hashlib.sha256(password).digest()),
        bcrypt.gensalt())
    with open("encryption/hash_pw.txt", "wb+") as txt:
        txt.write(hashed_pw)
        txt.close()


hash_password()
