import gravscale
from ..enum import EnumNetworkPrintableAttributes
from ...abstract import (
    AbstractReadInputValue,
    AbstractPrintableTable,
    AbstractPrintableJSON,
)


class ListNetworkPublicIps(
    AbstractReadInputValue, AbstractPrintableTable, AbstractPrintableJSON
):
    _printable_attributes = EnumNetworkPrintableAttributes
    _table_headers = [
        _printable_attributes.VPC_NAME.value,
        _printable_attributes.ADDRESS.value,
        _printable_attributes.PUBLIC_ADDRESS.value,
    ]

    def __init__(
        self, configuration: gravscale.Configuration, client_id: int, vpc_name: str
    ):
        self._configuration = configuration
        self._client_id = client_id
        self._vpc_name = vpc_name

    async def _validate(self):
        self._client_id = await self._read_prompt_input(
            self._printable_attributes.CLIENT_ID.value, self._client_id, int
        )
        self._vpc_name = await self._read_prompt_input(
            self._printable_attributes.VPC_NAME.value, self._vpc_name, str
        )

    async def _gen_table_rows(self, ips: dict):
        ips_info = []
        for ip in ips:
            for pubip in ip["publicIp"]:
                ips_info.append((ip["vpc"]["name"], ip["address"], pubip["address"]))
        return ips_info

    async def execute(self, return_json=False):
        await self._validate()
        with gravscale.ApiClient(self._configuration) as api_client:
            api_instance = gravscale.NetworkApi(api_client)
            ips = api_instance.list_all_public_ips(self._client_id, self._vpc_name)

        if return_json:
            await self._echo_json(ips.to_dict())
            return
        ips_info = await self._gen_table_rows(ips.to_dict()["items"])
        column_widths = await self._calculate_columns_width(
            self._table_headers, ips_info
        )
        await self._echo_table(column_widths, self._table_headers, ips_info)
