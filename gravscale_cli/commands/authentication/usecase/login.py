import click

import gravscale
from ...abstract import AbstractReadInputValue
from ....config import CliConfiguration
from ..enum import EnumAuthenticationPrintableAttributes


class LoginAuthenticateCommand(AbstractReadInputValue):
    _printable_attributes = EnumAuthenticationPrintableAttributes

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

        self._email = await self._read_prompt_input(
            self._printable_attributes.EMAIL.value, self._email, type=str
        )
        self._password = await self._read_prompt_input(
            self._printable_attributes.PASSWORD.value,
            self._password,
            type=str,
            hide_input=True,
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
