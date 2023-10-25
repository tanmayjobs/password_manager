import bcrypt


class Crypt:

    @staticmethod
    def hash(password: str) -> str:
        password_bytes = password
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password_bytes, salt)

        return password_hash

    @staticmethod
    def check(password: str, hashed_password: str):
        return bcrypt.checkpw(password, hashed_password)

    @staticmethod
    def encrypt(password: str):
        raise NotImplementedError

    @staticmethod
    def decrypt(password: str):
        raise NotImplementedError
