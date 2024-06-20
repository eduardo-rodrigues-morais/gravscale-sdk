# gravscale.NetworkApi

All URIs are relative to *http://under-dev-services.gravmanage.com/dev/public-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_public_ip**](NetworkApi.md#create_public_ip) | **POST** /api/network/public-ip | Create Public Ip
[**deallocate_public_ip**](NetworkApi.md#deallocate_public_ip) | **DELETE** /api/network/public-ip | Deallocate Public Ip
[**list_all_public_ips**](NetworkApi.md#list_all_public_ips) | **GET** /api/network/public-ip | List Public Ips


# **create_public_ip**
> TaskTreeSchema create_public_ip(client_id, create_public_ip_schema)

Create Public Ip

### Example

* Bearer Authentication (HTTPBearer):

```python
import gravscale
from gravscale.models.create_public_ip_schema import CreatePublicIpSchema
from gravscale.models.task_tree_schema import TaskTreeSchema
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
    api_instance = gravscale.NetworkApi(api_client)
    client_id = 56 # int | 
    create_public_ip_schema = gravscale.CreatePublicIpSchema() # CreatePublicIpSchema | 

    try:
        # Create Public Ip
        api_response = api_instance.create_public_ip(client_id, create_public_ip_schema)
        print("The response of NetworkApi->create_public_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkApi->create_public_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 
 **create_public_ip_schema** | [**CreatePublicIpSchema**](CreatePublicIpSchema.md)|  | 

### Return type

[**TaskTreeSchema**](TaskTreeSchema.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deallocate_public_ip**
> TaskTreeSchema deallocate_public_ip(client_id, address)

Deallocate Public Ip

### Example

* Bearer Authentication (HTTPBearer):

```python
import gravscale
from gravscale.models.task_tree_schema import TaskTreeSchema
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
    api_instance = gravscale.NetworkApi(api_client)
    client_id = 56 # int | 
    address = 'address_example' # str | 

    try:
        # Deallocate Public Ip
        api_response = api_instance.deallocate_public_ip(client_id, address)
        print("The response of NetworkApi->deallocate_public_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkApi->deallocate_public_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 
 **address** | **str**|  | 

### Return type

[**TaskTreeSchema**](TaskTreeSchema.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_public_ips**
> PagePublicIpSchema list_all_public_ips(client_id, vpc_name, page=page, size=size)

List Public Ips

### Example

* Bearer Authentication (HTTPBearer):

```python
import gravscale
from gravscale.models.page_public_ip_schema import PagePublicIpSchema
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
    api_instance = gravscale.NetworkApi(api_client)
    client_id = 56 # int | 
    vpc_name = 'vpc_name_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    size = 50 # int |  (optional) (default to 50)

    try:
        # List Public Ips
        api_response = api_instance.list_all_public_ips(client_id, vpc_name, page=page, size=size)
        print("The response of NetworkApi->list_all_public_ips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkApi->list_all_public_ips: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 
 **vpc_name** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **size** | **int**|  | [optional] [default to 50]

### Return type

[**PagePublicIpSchema**](PagePublicIpSchema.md)

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

