import gravscale


class LoginAuthenticateCommand:
    def __init__(
        self, email: str, password: str, configuration: gravscale.Configuration
    ):
        self._email = email
        self._password = password
        self._configuration = configuration

    async def execute(self) -> gravscale.AuthorizationSchema:
        with gravscale.ApiClient(self._configuration) as api_client:
            api_instance = gravscale.AuthenticationApi(api_client)
            login_schema = gravscale.LoginSchema(
                email=self._email, password=self._password
            )
            authorization = api_instance.sign_in(login_schema)
        return authorization
