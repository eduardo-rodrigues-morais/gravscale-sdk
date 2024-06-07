#from gravscale.client import GravscaleClient
import gravscale


class GetMetalsCommand:
    def __init__(
        self, configuration: gravscale.Configuration
    ):
        self._configuration = configuration

    async def execute(self):
        with gravscale.ApiClient(self._configuration) as api_client:
            api_instance = gravscale.MetalApi(api_client)
            metals = api_instance.get_metal()
        return metals
