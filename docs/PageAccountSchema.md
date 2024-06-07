# PageAccountSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AppModulesAccountSchemaAccountSchema]**](AppModulesAccountSchemaAccountSchema.md) |  | 
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 

## Example

```python
from gravscale.models.page_account_schema import PageAccountSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PageAccountSchema from a JSON string
page_account_schema_instance = PageAccountSchema.from_json(json)
# print the JSON string representation of the object
print(PageAccountSchema.to_json())

# convert the object into a dict
page_account_schema_dict = page_account_schema_instance.to_dict()
# create an instance of PageAccountSchema from a dict
page_account_schema_from_dict = PageAccountSchema.from_dict(page_account_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


