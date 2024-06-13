import asyncclick as click

from .commands.authentication.cli import authentication_group
from .commands.account.cli import account_group
from .commands.network.cli import nat11_group
from .commands.vpc.cli import vpc_group
from .config import CliConfiguration


@click.group()
@click.pass_context
def gravscale(ctx: click.Context) -> None:
    ctx.ensure_object(CliConfiguration)
    ctx.obj = {"config": CliConfiguration()}


gravscale.add_command(authentication_group)
gravscale.add_command(account_group)
gravscale.add_command(vpc_group)
gravscale.add_command(nat11_group)

if __name__ == "__main__":
    gravscale(obj={})
