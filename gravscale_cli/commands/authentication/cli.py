import asyncclick as click

from ... import CliConfiguration
from .usecase import LoginAuthenticateCommand, AuthenticateInfoCommand


@click.group(name="auth")
async def authentication_group():
    """Authentication"""
    pass


@authentication_group.command("login", help="Authenticate user by email and password")
@click.option(
    "--config-file",
    "-c",
    type=click.Path(exists=True),
    default=None,
    help="Configuration file",
)
@click.option("--email", "-e", required=False, type=str, help="User email")
@click.option("--password", "-p", required=False, type=str, help="User password")
@click.pass_obj
async def login(obj, email: str, password: str, config_file: str):
    cli_config: CliConfiguration = obj["config"]
    await LoginAuthenticateCommand(email, password, config_file, cli_config).execute()


@authentication_group.command(
    "info", help="Gets information from the user who is authenticated"
)
@click.pass_obj
async def auth_info(obj: dict):
    cli_config: CliConfiguration = obj["config"]
    await AuthenticateInfoCommand(cli_config.load_sdk_configuration()).execute()
