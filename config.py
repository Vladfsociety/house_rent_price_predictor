import json
import os


class Config:
    def __init__(self):
        self.project_root = os.path.abspath(os.path.dirname(__file__))
        config_path = os.path.join(self.project_root, 'config.json')
        with open(config_path, 'r') as config_file:
            self._config = json.load(config_file)

    def get_path(self, key):
        if key not in self._config:
            raise KeyError(f"Path '{key}' not found in configuration")
        return os.path.join(self.project_root, self._config[key])

config = Config()