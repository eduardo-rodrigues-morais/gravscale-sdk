import ipaddress

import gravscale
from ..enum import EnumNetworkPrintableAttributes
from ...abstract import (
    AbstractReadInputValue,
)


class DeallocateNetworkPublicIp(AbstractReadInputValue):
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
            self._printable_attributes.CLIENT_ID.value, self._client_id, int
        )
        self._address = await self._read_prompt_input(
            self._printable_attributes.ADDRESS.value,
            self._address,
            str,
            [(ipaddress.ip_address, "The address IP is invalid")],
        )

    async def execute(self):
        await self._validate()
        with gravscale.ApiClient(self._configuration) as api_client:
            api_instance = gravscale.NetworkApi(api_client)
            task = api_instance.deallocate_public_ip(self._client_id, self._address)
            print(task.to_dict())
