import click

import gravscale


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
