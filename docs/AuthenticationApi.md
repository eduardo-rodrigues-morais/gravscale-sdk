# gravscale.AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sign_in**](AuthenticationApi.md#sign_in) | **POST** /api/auth/sign-in | Sign In
[**sign_up**](AuthenticationApi.md#sign_up) | **POST** /api/auth/sign-up | Sign Up


# **sign_in**
> AuthorizationSchema sign_in(login_schema)

Sign In

<p>Este endpoint é dedicado à autenticação dos usuários na API do serviço de contratação de servidores bare metal. Para realizar a autenticação, não são necessários parâmetros de consulta ou cabeçalho específicos. No entanto, espera-se um corpo de requisição do tipo \"application/json\" contendo um esquema JSON com os campos obrigatórios \"email\" e \"password\", ambos do tipo \"string\".</p>     <p>Os dados de autenticação devem ser fornecidos de maneira segura e estruturada no corpo da requisição para garantir a verificação correta da identidade do usuário.</p>     <p>Além disso, são definidos dois códigos de resposta HTTP para este endpoint, indicando diferentes situações ou resultados possíveis durante o processo de autenticação.</p>

### Example


```python
import gravscale
from gravscale.models.authorization_schema import AuthorizationSchema
from gravscale.models.login_schema import LoginSchema
from gravscale.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gravscale.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with gravscale.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gravscale.AuthenticationApi(api_client)
    login_schema = gravscale.LoginSchema() # LoginSchema | 

    try:
        # Sign In
        api_response = api_instance.sign_in(login_schema)
        print("The response of AuthenticationApi->sign_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->sign_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_schema** | [**LoginSchema**](LoginSchema.md)|  | 

### Return type

[**AuthorizationSchema**](AuthorizationSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_up**
> AccountSchema sign_up(login_schema)

Sign Up

<p>Este endpoint destina-se ao processo de registro de novos clientes na API do serviço de contratação de servidores bare metal. Durante a chamada deste endpoint, não são requeridos parâmetros de consulta ou cabeçalho específicos. No entanto, é fundamental fornecer um corpo de requisição no formato \"application/json\" contendo um esquema JSON estruturado.</p>     <p>No corpo da requisição, são esperados os campos obrigatórios \"email\" e \"password\", ambos do tipo \"string\". É essencial que as informações fornecidas sigam o formato adequado para garantir a correta criação do novo cadastro de cliente.</p>     <p>Ao utilizar este endpoint, é possível efetuar o registro de novos clientes de maneira eficiente e segura, permitindo a expansão da base de usuários do serviço de servidores bare metal.</p>

### Example


```python
import gravscale
from gravscale.models.account_schema import AccountSchema
from gravscale.models.login_schema import LoginSchema
from gravscale.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gravscale.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with gravscale.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gravscale.AuthenticationApi(api_client)
    login_schema = gravscale.LoginSchema() # LoginSchema | 

    try:
        # Sign Up
        api_response = api_instance.sign_up(login_schema)
        print("The response of AuthenticationApi->sign_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->sign_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_schema** | [**LoginSchema**](LoginSchema.md)|  | 

### Return type

[**AccountSchema**](AccountSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

