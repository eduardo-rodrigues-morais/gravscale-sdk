import asyncclick as click

from .commands.auth import LoginAuthenticateCommand
from .config import CliConfiguration


@click.group(chain=True)
@click.pass_context
def gravscale(ctx) -> None:
    ctx.obj = {"config": CliConfiguration()}


@gravscale.command()
@click.option(
    "--email",
    default=None,
    help="User email",
)
@click.option(
    "--password",
    default=None,
    help="User password",
)
@click.option(
    "--config-file",
    default=None,
    help="The configuration file",
)
@click.pass_obj
async def login(obj, email: str, password: str, config_file: str):
    cli_config: CliConfiguration = obj["config"]
    authorization = await LoginAuthenticateCommand(
        email, password, cli_config.load_sdk_configuration()
    ).execute()
    cli_config.save_authorization(authorization)
    click.echo("User successfully authenticated!")


@gravscale.command()
@click.pass_obj
async def get_metal(obj):
    cli_config: CliConfiguration = obj["config"]
    grav_config = cli_config.load_sdk_configuration()
    print(grav_config.auth_settings())

    # click.echo(ctx.obj)
    # await GetMetalsCommand().execute()


if __name__ == "__main__":
    gravscale(obj={})
