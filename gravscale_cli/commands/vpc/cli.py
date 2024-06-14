import asyncclick as click

from ... import CliConfiguration
from .usecase.list_vpc import ListVpcCommand


@click.group(name="vpc")
async def vpc_group():
    """Virtual Private Cloud"""
    pass


@vpc_group.command("list")
@click.option("--client-id", "-c", required=False, type=int, help="Client ID")
@click.option(
    "--json",
    "-j",
    is_flag=True,
    default=False,
    type=bool,
    help="Returned result as JSON",
)
@click.pass_obj
async def list_vpc_command(obj, client_id: int, json: bool):
    cli_config: CliConfiguration = obj["config"]
    await ListVpcCommand(cli_config.load_sdk_configuration(), client_id).execute(
        return_json=json
    )
