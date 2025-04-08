from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self, key: bytes):
        self.fernet = Fernet(key)

    def encrypt(self, plaintext: str) -> str:
        return self.fernet.encrypt(plaintext.encode()).decode()

    def decrypt(self, ciphertext: str) -> str:
        return self.fernet.decrypt(ciphertext.encode()).decode()

    def encrypt_dict(self, data: dict) -> dict:
        return {k: self.encrypt(v) for k, v in data.items()}

    def decrypt_dict(self, data: dict) -> dict:
        return {k: self.decrypt(v) for k, v in data.items()}

    def update_key(self, key: bytes):
        self.fernet = Fernet(key)
