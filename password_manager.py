from key_manager import KeyManager
from encryptor import Encryptor
from vault_storage import VaultStorage
from vault import Vault

class PasswordManager:
    def __init__(self, master_password: str):
        self.key_manager = KeyManager(master_password)
        self.encryptor = Encryptor(self.key_manager.get_key())
        self.storage = VaultStorage()
        self.data = self.storage.load()

        if 'master' in self.data:
            try:
                self.encryptor.decrypt(self.data['master'])
            except:
                raise ValueError("Invalid master password")
        else:
            self.data['master'] = self.encryptor.encrypt("master_check")

        self.vault = Vault(self.data, self.encryptor)

    def add_service(self, service, username, password):
        self.vault.add_entry(service, username, password)
        self.save()

    def get_service(self, service):
        return self.vault.get_entry(service)

    def list_services(self):
        return self.vault.list_services()

    def update_service(self, service, username=None, password=None):
        self.vault.update_entry(service, username, password)
        self.save()

    def delete_service(self, service):
        self.vault.delete_entry(service)
        self.save()

    def save(self):
        self.storage.save(self.data)
