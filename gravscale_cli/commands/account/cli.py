import asyncclick as click

from ... import CliConfiguration
from .usecase import ListAccountsCommand


@click.group(name="account")
async def account_group():
    """Client Accounts"""
    pass


@account_group.command("list")
@click.option(
    "--json",
    "-j",
    is_flag=True,
    default=False,
    type=bool,
    help="Returned result as JSON",
)
@click.pass_obj
async def list_accounts(obj, json: bool):
    cli_config: CliConfiguration = obj["config"]
    await ListAccountsCommand(cli_config.load_sdk_configuration()).execute(
        return_json=json
    )
