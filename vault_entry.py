class VaultEntry:
    def __init__(self, service: str, username: str, password: str):
        self.service = service
        self.username = username
        self.password = password

    def to_dict(self, encryptor):
        return {
            'username': encryptor.encrypt(self.username),
            'password': encryptor.encrypt(self.password)
        }

    @staticmethod
    def from_dict(service: str, data: dict, encryptor):
        username = encryptor.decrypt(data['username'])
        password = encryptor.decrypt(data['password'])
        return VaultEntry(service, username, password)

    def update_username(self, new_username):
        self.username = new_username

    def update_password(self, new_password):
        self.password = new_password

    def get_summary(self):
        return f"{self.service}: {self.username}"
