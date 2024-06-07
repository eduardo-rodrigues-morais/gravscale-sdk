# AppModulesVpcSchemaVpcSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**tenant** | [**TenantSchema**](TenantSchema.md) |  | 

## Example

```python
from gravscale.models.app_modules_vpc_schema_vpc_schema import AppModulesVpcSchemaVpcSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AppModulesVpcSchemaVpcSchema from a JSON string
app_modules_vpc_schema_vpc_schema_instance = AppModulesVpcSchemaVpcSchema.from_json(json)
# print the JSON string representation of the object
print(AppModulesVpcSchemaVpcSchema.to_json())

# convert the object into a dict
app_modules_vpc_schema_vpc_schema_dict = app_modules_vpc_schema_vpc_schema_instance.to_dict()
# create an instance of AppModulesVpcSchemaVpcSchema from a dict
app_modules_vpc_schema_vpc_schema_from_dict = AppModulesVpcSchemaVpcSchema.from_dict(app_modules_vpc_schema_vpc_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


