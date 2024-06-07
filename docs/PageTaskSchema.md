# PageTaskSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TaskSchema]**](TaskSchema.md) |  | 
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 

## Example

```python
from gravscale.models.page_task_schema import PageTaskSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PageTaskSchema from a JSON string
page_task_schema_instance = PageTaskSchema.from_json(json)
# print the JSON string representation of the object
print(PageTaskSchema.to_json())

# convert the object into a dict
page_task_schema_dict = page_task_schema_instance.to_dict()
# create an instance of PageTaskSchema from a dict
page_task_schema_from_dict = PageTaskSchema.from_dict(page_task_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


