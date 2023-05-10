import bcrypt


def hash_password(password: str) -> bytes:
    password_bytes = bytes(password, "utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt)


def check_password(password: str, hashed_password: bytes) -> bool:
    password_bytes = bytes(password, "utf-8")
    return bcrypt.checkpw(password_bytes, hashed_password)
