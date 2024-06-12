import click

import gravscale
from ..config import CliConfiguration


class LoginAuthenticateCommand:
    def __init__(
        self, email: str, password: str, config_file: str, cli_config: CliConfiguration
    ):
        self._email = email
        self._password = password
        self._config_file = config_file
        self._cli_config = cli_config

    async def _validate(self):
        if self._config_file:
            data = self._cli_config.read_user_config(self._config_file)
            self._email = data["gravscale"]["email"]
            self._password = data["gravscale"]["password"]
            return

        self._email = (
            click.prompt("Email", type=str) if not self._email else self._email
        )
        self._password = (
            click.prompt("Password", hide_input=True, type=str)
            if not self._password
            else self._password
        )

    async def execute(self):
        await self._validate()
        with gravscale.ApiClient(
            self._cli_config.load_sdk_configuration()
        ) as api_client:
            api_instance = gravscale.AuthenticationApi(api_client)
            login_schema = gravscale.LoginSchema(
                email=self._email, password=self._password
            )
            authorization = api_instance.sign_in(login_schema)
        self._cli_config.save_authorization(authorization)
        click.echo("User successfully authenticated!")


class AuthenticateInfoCommand:
    def __init__(self, configuration: gravscale.Configuration):
        self._configuration = configuration

    async def execute(self):
        with gravscale.ApiClient(self._configuration) as api_client:
            api_instance = gravscale.AuthenticationApi(api_client)
            authenticated_user_info = api_instance.info()
        click.echo(
            f"Authenticated user: {authenticated_user_info.email} {authenticated_user_info.nickname}"
        )
