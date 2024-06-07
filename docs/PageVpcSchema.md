# PageVpcSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AppModulesVpcSchemaVpcSchema]**](AppModulesVpcSchemaVpcSchema.md) |  | 
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 

## Example

```python
from gravscale.models.page_vpc_schema import PageVpcSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PageVpcSchema from a JSON string
page_vpc_schema_instance = PageVpcSchema.from_json(json)
# print the JSON string representation of the object
print(PageVpcSchema.to_json())

# convert the object into a dict
page_vpc_schema_dict = page_vpc_schema_instance.to_dict()
# create an instance of PageVpcSchema from a dict
page_vpc_schema_from_dict = PageVpcSchema.from_dict(page_vpc_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


