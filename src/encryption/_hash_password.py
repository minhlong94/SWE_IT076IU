import base64
import hashlib

import bcrypt


def hash_password(encryption_path="src/encryption"):
    """Hash password function

    This file helps to hash the password using bcrypt.

    Returns:
        None
    """
    password = "python"
    hashed_pw = bcrypt.hashpw(base64.b64encode(hashlib.sha256(password.encode()).digest()), bcrypt.gensalt())
    with open(f"{encryption_path}/hash_pw", "w+b") as f:
        f.write(hashed_pw)


hash_password("encryption")
