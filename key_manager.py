import base64
from hashlib import sha256

class KeyManager:
    def __init__(self, master_password: str):
        self.master_password = master_password
        self.key = self.derive_key(master_password)

    def derive_key(self, password: str) -> bytes:
        hash_digest = sha256(password.encode()).digest()
        return base64.urlsafe_b64encode(hash_digest)

    def get_key(self):
        return self.key

    def update_password(self, new_password: str):
        self.master_password = new_password
        self.key = self.derive_key(new_password)

    def is_same_password(self, password: str):
        return self.derive_key(password) == self.key
