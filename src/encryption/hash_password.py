import base64
import hashlib

import bcrypt

password = b"py"
hashed_pw = bcrypt.hashpw(
    base64.b64encode(hashlib.sha256(password).digest()),
    bcrypt.gensalt())
with open("hash_pw.txt", "wb+") as txt:
    txt.write(hashed_pw)
    txt.close()
