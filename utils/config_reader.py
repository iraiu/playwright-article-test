import json
import os


class ConfigReader:
    _instance = None
    _config = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "config.json"
        )
        with open(config_path, 'r', encoding='utf-8') as f:
            self._config = json.load(f)

    def get(self, key, default=None):
        keys = key.split('.')
        value = self._config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value

    @property
    def base_url(self):
        return self.get("base_url")

    @property
    def headless(self):
        return self.get("playwright.headless", False)

    @property
    def viewport(self):
        return self.get("playwright.viewport", {"width": 1280, "height": 720})

    @property
    def slow_mo(self):
        return self.get("slow_mo", 0)


config = ConfigReader()