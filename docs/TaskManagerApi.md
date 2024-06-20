# gravscale.TaskManagerApi

All URIs are relative to *http://under-dev-services.gravmanage.com/dev/public-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task**](TaskManagerApi.md#get_task) | **GET** /api/task/{task_id} | Get Task
[**list_tasks**](TaskManagerApi.md#list_tasks) | **GET** /api/task/ | List Tasks


# **get_task**
> TaskTreeSchema get_task(task_id, client_id)

Get Task

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
    api_instance = gravscale.TaskManagerApi(api_client)
    task_id = 'task_id_example' # str | 
    client_id = 56 # int | 

    try:
        # Get Task
        api_response = api_instance.get_task(task_id, client_id)
        print("The response of TaskManagerApi->get_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskManagerApi->get_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **client_id** | **int**|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks**
> PageTaskTreeSchema list_tasks(client_id, correlation_id=correlation_id, status=status, created_at=created_at, updated_at=updated_at, page=page, size=size)

List Tasks

### Example

* Bearer Authentication (HTTPBearer):

```python
import gravscale
from gravscale.models.page_task_tree_schema import PageTaskTreeSchema
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
    api_instance = gravscale.TaskManagerApi(api_client)
    client_id = 56 # int | 
    correlation_id = 'correlation_id_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    created_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    updated_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    page = 1 # int |  (optional) (default to 1)
    size = 50 # int |  (optional) (default to 50)

    try:
        # List Tasks
        api_response = api_instance.list_tasks(client_id, correlation_id=correlation_id, status=status, created_at=created_at, updated_at=updated_at, page=page, size=size)
        print("The response of TaskManagerApi->list_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskManagerApi->list_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 
 **correlation_id** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **created_at** | **datetime**|  | [optional] 
 **updated_at** | **datetime**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **size** | **int**|  | [optional] [default to 50]

### Return type

[**PageTaskTreeSchema**](PageTaskTreeSchema.md)

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

