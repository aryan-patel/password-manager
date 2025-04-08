import os
import json

class VaultStorage:
    def __init__(self, file_path='vault.json'):
        self.file_path = file_path

    def load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                return json.load(f)
        return {}

    def save(self, data: dict):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=2)

    def clear(self):
        with open(self.file_path, 'w') as f:
            f.write("{}")

    def exists(self):
        return os.path.exists(self.file_path)

    def get_path(self):
        return self.file_path
