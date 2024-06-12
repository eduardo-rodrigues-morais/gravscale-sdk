import asyncclick as click

from .config import CliConfiguration
from .commands import (
    LoginAuthenticateCommand,
    AuthenticateInfoCommand,
    ListVpcCommand,
    ListAccountsCommand,
    ListNetworkPublicIps,
    CreateNetworkPublicIp,
    DeallocateNetworkPublicIp,
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


@gravscale.command(help="Gets information from the user who is authenticated")
@click.pass_obj
async def auth_info(obj: dict):
    cli_config: CliConfiguration = obj["config"]
    await AuthenticateInfoCommand(cli_config.load_sdk_configuration()).execute()


@gravscale.command()
@click.option("--json", "-j", default=False, type=bool, help="Returned result as JSON")
@click.pass_obj
async def list_accounts(obj, json: bool):
    cli_config: CliConfiguration = obj["config"]
    await ListAccountsCommand(cli_config.load_sdk_configuration()).execute(
        return_json=json
    )


@gravscale.command()
@click.option("--client-id", "-c", required=False, type=int, help="Client ID")
@click.option("--json", "-j", default=False, type=bool, help="Returned result as JSON")
@click.pass_obj
async def list_vpc(obj, client_id: int, json: bool):
    cli_config: CliConfiguration = obj["config"]
    await ListVpcCommand(cli_config.load_sdk_configuration(), client_id).execute(
        return_json=json
    )


@gravscale.command()
@click.option("--client-id", "-c", required=False, type=int, help="Client ID")
@click.option("--vpc-name", "-v", required=False, type=str, help="VPC name")
@click.option("--json", "-j", default=False, type=bool, help="Returned result as JSON")
@click.pass_obj
async def list_publicip(obj, client_id: int, vpc_name: str, json: bool):
    cli_config: CliConfiguration = obj["config"]
    await ListNetworkPublicIps(
        cli_config.load_sdk_configuration(), client_id, vpc_name
    ).execute(return_json=json)


@gravscale.command()
@click.option("--client-id", "-c", required=False, type=int, help="Client ID")
@click.option("--vpc-name", "-v", required=False, type=str, help="VPC name")
@click.option("--address", "-a", required=False, type=str, help="IP Address")
@click.pass_obj
async def create_publicip(obj, client_id: int, vpc_name: str, address: str):
    cli_config: CliConfiguration = obj["config"]
    await CreateNetworkPublicIp(
        cli_config.load_sdk_configuration(), client_id, vpc_name, address
    ).execute()


@gravscale.command()
@click.option("--client-id", "-c", required=False, type=int, help="Client ID")
@click.option("--address", "-a", required=False, type=str, help="Public IP Address")
@click.pass_obj
async def deallocate_publicip(obj, client_id: int, address: str):
    cli_config: CliConfiguration = obj["config"]
    await DeallocateNetworkPublicIp(
        cli_config.load_sdk_configuration(), client_id, address
    ).execute()


if __name__ == "__main__":
    gravscale(obj={})
