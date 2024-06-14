import asyncclick as click

from ... import CliConfiguration
from .usecase import (
    ListNetworkPublicIps,
    CreateNetworkPublicIp,
    DeallocateNetworkPublicIp,
)


@click.group(name="nat11")
async def nat11_group():
    """Network Address Translation"""
    pass


@nat11_group.command("list")
@click.option("--client-id", "-c", required=False, type=int, help="Client ID")
@click.option("--vpc-name", "-v", required=False, type=str, help="VPC name")
@click.option(
    "--json",
    "-j",
    is_flag=True,
    default=False,
    type=bool,
    help="Returned result as JSON",
)
@click.pass_obj
async def list_publicip(obj, client_id: int, vpc_name: str, json: bool):
    cli_config: CliConfiguration = obj["config"]
    await ListNetworkPublicIps(
        cli_config.load_sdk_configuration(), client_id, vpc_name
    ).execute(return_json=json)


@nat11_group.command("allocate")
@click.option("--client-id", "-c", required=False, type=int, help="Client ID")
@click.option("--vpc-name", "-v", required=False, type=str, help="VPC name")
@click.option("--address", "-a", required=False, type=str, help="IP Address")
@click.pass_obj
async def allocate_publicip(obj, client_id: int, vpc_name: str, address: str):
    cli_config: CliConfiguration = obj["config"]
    await CreateNetworkPublicIp(
        cli_config.load_sdk_configuration(), client_id, vpc_name, address
    ).execute()


@nat11_group.command("deallocate")
@click.option("--client-id", "-c", required=False, type=int, help="Client ID")
@click.option("--address", "-a", required=False, type=str, help="Public IP Address")
@click.pass_obj
async def deallocate_publicip(obj, client_id: int, address: str):
    cli_config: CliConfiguration = obj["config"]
    await DeallocateNetworkPublicIp(
        cli_config.load_sdk_configuration(), client_id, address
    ).execute()
