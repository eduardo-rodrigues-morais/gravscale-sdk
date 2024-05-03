from pathlib import Path
import os
import json
import gravscale as grav_sdk


class CliConfiguration:
    host = "http://under-dev-services.gravmanage.com/dev/public-api"

    def __init__(self):
        self._config_path = self._get_config_path()

    @classmethod
    def _get_config_path(cls):
        return os.path.join(str(Path.home()), ".gravscale/")

    def _ensure_config_directory(self):
        config_dir = os.path.dirname(self._config_path)
        os.makedirs(config_dir, exist_ok=True)

    def _load_authorization(self) -> dict:
        try:
            with open(os.path.join(self._config_path, ".auth.json"), "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return {}

    def save_authorization(self, authorization: grav_sdk.AuthorizationSchema):
        self._ensure_config_directory()
        with open(os.path.join(self._config_path, ".auth.json"), "w") as file:
            json.dump({"access_token": authorization.access_token}, file)

    def load_sdk_configuration(self) -> grav_sdk.Configuration:
        auth_data = self._load_authorization()
        return grav_sdk.Configuration(host=self.host, **auth_data)
