import ipaddress
from time import sleep

import click
from tqdm import tqdm

import gravscale
from ..enum import EnumNetworkPrintableAttributes
from ...abstract import AbstractReadInputValue, AbstractTask, AbstractPrintableTask


class CreateNetworkPublicIp(
    AbstractReadInputValue, AbstractTask, AbstractPrintableTask
):
    _printable_attributes = EnumNetworkPrintableAttributes

    def __init__(
        self,
        configuration: gravscale.Configuration,
        client_id: int,
        vpc_name: str,
        address: str,
    ):
        self._configuration = configuration
        self._client_id = client_id
        self._vpc_name = vpc_name
        self._address = address

    async def _validate(self):
        self._client_id = await self._read_prompt_input(
            self._printable_attributes.CLIENT_ID.value, self._client_id, type=int
        )
        self._vpc_name = await self._read_prompt_input(
            self._printable_attributes.VPC_NAME.value, self._vpc_name, type=str
        )
        self._address = await self._read_prompt_input(
            self._printable_attributes.ADDRESS.value,
            self._address,
            type=str,
            validators=[(ipaddress.ip_address, "The address IP is invalid")],
        )

    @classmethod
    async def _filter_sub_task_ip_allocate(cls, task):
        sub_task_ip_allocate = [
            t for t in task.sub_tasks if t.action == "public_ip.allocate"
        ]
        task.result = (
            sub_task_ip_allocate.pop().result if sub_task_ip_allocate else None
        )

    async def execute(self):
        await self._validate()
        with gravscale.ApiClient(self._configuration) as api_client:
            api_instance = gravscale.NetworkApi(api_client)
            click.echo("Start public ip allocation process...")
            task = api_instance.create_public_ip(
                self._client_id,
                gravscale.CreatePublicIpSchema(
                    vpc_name=self._vpc_name, address=self._address
                ),
            )
            task = await self.await_task_complete(api_client, self._client_id, task)
            await self._filter_sub_task_ip_allocate(task)
            await self._echo_task_info(task)
