# gravscale.AccountApi

All URIs are relative to *http://under-dev-services.gravmanage.com/dev/public-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account**](AccountApi.md#get_account) | **GET** /api/account/ | Get Account
[**list_accounts**](AccountApi.md#list_accounts) | **GET** /api/account/all | List All Accounts


# **get_account**
> AppModulesAccountSchemaAccountSchema get_account(uuid=uuid, client_id=client_id)

Get Account

### Example

* Bearer Authentication (HTTPBearer):

```python
import gravscale
from gravscale.models.app_modules_account_schema_account_schema import AppModulesAccountSchemaAccountSchema
from gravscale.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://under-dev-services.gravmanage.com/dev/public-api
# See configuration.py for a list of all supported configuration parameters.
configuration = gravscale.Configuration(
    host = "http://under-dev-services.gravmanage.com/dev/public-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = gravscale.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gravscale.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gravscale.AccountApi(api_client)
    uuid = 'uuid_example' # str |  (optional)
    client_id = 56 # int |  (optional)

    try:
        # Get Account
        api_response = api_instance.get_account(uuid=uuid, client_id=client_id)
        print("The response of AccountApi->get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | [optional] 
 **client_id** | **int**|  | [optional] 

### Return type

[**AppModulesAccountSchemaAccountSchema**](AppModulesAccountSchemaAccountSchema.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_accounts**
> PageAccountSchema list_accounts(page=page, size=size)

List All Accounts

### Example

* Bearer Authentication (HTTPBearer):

```python
import gravscale
from gravscale.models.page_account_schema import PageAccountSchema
from gravscale.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://under-dev-services.gravmanage.com/dev/public-api
# See configuration.py for a list of all supported configuration parameters.
configuration = gravscale.Configuration(
    host = "http://under-dev-services.gravmanage.com/dev/public-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = gravscale.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gravscale.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gravscale.AccountApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    size = 50 # int |  (optional) (default to 50)

    try:
        # List All Accounts
        api_response = api_instance.list_accounts(page=page, size=size)
        print("The response of AccountApi->list_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->list_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **size** | **int**|  | [optional] [default to 50]

### Return type

[**PageAccountSchema**](PageAccountSchema.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

