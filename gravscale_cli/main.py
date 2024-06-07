import asyncclick as click

from .config import CliConfiguration
from .commands import (
    LoginAuthenticateCommand,
    AuthenticateInfoCommand,
)


@click.group(chain=True)
@click.pass_context
def gravscale(ctx) -> None:
    ctx.obj = {"config": CliConfiguration()}


@gravscale.command(help="Authenticate user by email and password")
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
    click.echo("User successfully authenticated!")


@gravscale.command(help="Gets information from the user who is authenticated")
@click.pass_obj
async def auth_info(obj: dict):
    cli_config: CliConfiguration = obj["config"]
    user = await AuthenticateInfoCommand(cli_config.load_sdk_configuration()).execute()
    click.echo(f"Authenticated user: {user.email} {user.nickname}")


@gravscale.command()
@click.pass_obj
async def list_vpc(obj: dict):
    cli_config: CliConfiguration = obj["config"]


if __name__ == "__main__":
    gravscale(obj={})
