import ipaddress

import click

import gravscale
from ..enum import EnumNetworkPrintableAttributes
from ...abstract import AbstractReadInputValue, AbstractTask, AbstractPrintableTask


class DeallocateNetworkPublicIp(
    AbstractReadInputValue, AbstractTask, AbstractPrintableTask
):
    _printable_attributes = EnumNetworkPrintableAttributes

    def __init__(
        self,
        configuration: gravscale.Configuration,
        client_id: int,
        address: str,
    ):
        self._configuration = configuration
        self._client_id = client_id
        self._address = address

    async def _validate(self):
        self._client_id = await self._read_prompt_input(
            self._printable_attributes.CLIENT_ID.value, self._client_id, type=int
        )
        self._address = await self._read_prompt_input(
            self._printable_attributes.ADDRESS.value,
            self._address,
            type=str,
            validators=[(ipaddress.ip_address, "The address IP is invalid")],
        )

    async def execute(self):
        await self._validate()
        with gravscale.ApiClient(self._configuration) as api_client:
            network_api = gravscale.NetworkApi(api_client)
            click.echo("Start public ip deallocate process...")
            task = network_api.deallocate_public_ip(self._client_id, self._address)
            task = await self.await_task_complete(api_client, self._client_id, task)
            await self._echo_task_info(task)
