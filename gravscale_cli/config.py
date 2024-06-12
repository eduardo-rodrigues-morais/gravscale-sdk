from datetime import datetime
from pathlib import Path
import os
import json
import toml
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
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return {}

    def _handle_expired_access_token(self, auth: dict):
        now = datetime.now()
        expiration = datetime.fromisoformat(auth["expires_at"])
        if now > expiration:
            configuration = grav_sdk.Configuration(host=self.host)
            try:
                with grav_sdk.ApiClient(configuration) as api_client:
                    api_instance = grav_sdk.AuthenticationApi(api_client)
                    authorization = api_instance.refresh_token(auth["refresh_token"])
                    self.save_authorization(authorization)
                    return authorization.access_token
            except grav_sdk.exceptions.ForbiddenException:
                return None
        return auth["access_token"]

    def save_authorization(self, authorization: grav_sdk.AuthorizationSchema):
        self._ensure_config_directory()
        with open(os.path.join(self._config_path, ".auth.json"), "w") as file:
            json.dump(authorization.dict(), file, default=str)

    def load_sdk_configuration(self) -> grav_sdk.Configuration:
        config = {"host": self.host}
        auth = self._load_authorization()
        if len(auth.keys()) > 0:
            access_token = self._handle_expired_access_token(auth)
            if access_token:
                config["access_token"] = access_token
        return grav_sdk.Configuration(**config)

    @classmethod
    def read_user_config(cls, path_config_file: str):
        with open(path_config_file, "r") as file:
            config = toml.load(file)
        return config
