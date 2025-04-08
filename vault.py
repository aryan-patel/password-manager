from vault_entry import VaultEntry

class Vault:
    def __init__(self, data: dict, encryptor):
        self.data = data
        self.encryptor = encryptor

    def add_entry(self, service, username, password):
        entry = VaultEntry(service, username, password)
        self.data[service] = entry.to_dict(self.encryptor)

    def get_entry(self, service):
        if service in self.data:
            return VaultEntry.from_dict(service, self.data[service], self.encryptor)
        return None

    def update_entry(self, service, username=None, password=None):
        entry = self.get_entry(service)
        if entry:
            if username:
                entry.update_username(username)
            if password:
                entry.update_password(password)
            self.data[service] = entry.to_dict(self.encryptor)

    def delete_entry(self, service):
        if service in self.data:
            del self.data[service]

    def list_services(self):
        return [s for s in self.data if s != 'master']
