from typing import List

import click
import gravscale

from ...abstract import (
    AbstractPrintableTable,
    AbstractPrintableJSON,
    AbstractReadInputValue,
)
from ...network.enum import EnumNetworkPrintableAttributes


class ListVpcCommand(
    AbstractReadInputValue, AbstractPrintableTable, AbstractPrintableJSON
):
    _printable_attributes = EnumNetworkPrintableAttributes
    _table_headers = ["VPC Name", "Tenant Name", "Datacenter"]

    def __init__(self, configuration: gravscale.Configuration, client_id: int):
        self._configuration = configuration
        self._client_id = client_id

    async def _validate(self):
        self._client_id = await self._read_prompt_input(
            self._printable_attributes.CLIENT_ID.value, self._client_id, type=int
        )

    async def _gen_table_rows(self, vpcs: List[dict]):
        vpc_info = []
        for vpc in vpcs:
            vpc_info.append(
                (vpc["name"], vpc["tenant"]["name"], vpc["tenant"]["group"]["name"])
            )
        return vpc_info

    async def execute(self, return_json=False):
        await self._validate()
        with gravscale.ApiClient(self._configuration) as api_client:
            api_instance = gravscale.VirtualPrivateCloudApi(api_client)
            client_vpcs = api_instance.list_vpc(self._client_id)

        if return_json:
            await self._echo_json(client_vpcs.to_dict())
            return

        vpc_info = await self._gen_table_rows(client_vpcs.to_dict()["items"])
        column_widths = await self._calculate_columns_width(
            self._table_headers, vpc_info
        )
        await self._echo_table(column_widths, self._table_headers, vpc_info)
