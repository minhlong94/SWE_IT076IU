import base64
import hashlib
import os.path

import bcrypt


def hash_password(encryption_path="src/encryption"):
    """Hash password function

    This file helps to hash the password using bcrypt.

    Returns:
        None
    """
    password = "python"
    hashed_pw = bcrypt.hashpw(base64.b64encode(hashlib.sha256(password.encode()).digest()), bcrypt.gensalt())
    if not os.path.exists(f"{encryption_path}/hash_pw"):
        with open(f"{encryption_path}/hash_pw", "wb+") as f:
            f.write(hashed_pw)
    if not os.path.exists(f"{encryption_path}/check_session"):
        with open(f"{encryption_path}/check_session", "wb+"):
            pass
