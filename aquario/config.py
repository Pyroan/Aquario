import json

class Config:
    def __init__(self, path):
        with open(path) as f:
            self.json = json.load(f)

    def __getattr__(self, key):
        return self.json[key]

CONFIG = Config("aquario/config.json")