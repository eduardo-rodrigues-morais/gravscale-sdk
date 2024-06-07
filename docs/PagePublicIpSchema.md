# PagePublicIpSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PublicIpSchema]**](PublicIpSchema.md) |  | 
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 

## Example

```python
from gravscale.models.page_public_ip_schema import PagePublicIpSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PagePublicIpSchema from a JSON string
page_public_ip_schema_instance = PagePublicIpSchema.from_json(json)
# print the JSON string representation of the object
print(PagePublicIpSchema.to_json())

# convert the object into a dict
page_public_ip_schema_dict = page_public_ip_schema_instance.to_dict()
# create an instance of PagePublicIpSchema from a dict
page_public_ip_schema_from_dict = PagePublicIpSchema.from_dict(page_public_ip_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


