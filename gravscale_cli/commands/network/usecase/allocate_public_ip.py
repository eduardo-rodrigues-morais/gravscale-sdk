import ipaddress

import gravscale
from ..enum import EnumNetworkPrintableAttributes
from ...abstract import (
    AbstractReadInputValue,
)


class CreateNetworkPublicIp(AbstractReadInputValue):
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

    async def execute(self):
        await self._validate()
        with gravscale.ApiClient(self._configuration) as api_client:
            api_instance = gravscale.NetworkApi(api_client)
            task = api_instance.create_public_ip(
                self._client_id,
                gravscale.CreatePublicIpSchema(
                    vpc_name=self._vpc_name, address=self._address
                ),
            )
            print(task.to_dict())
