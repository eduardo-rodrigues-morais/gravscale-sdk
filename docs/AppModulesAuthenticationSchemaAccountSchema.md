# AppModulesAuthenticationSchemaAccountSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**email** | **str** |  | 
**nickname** | **str** |  | 
**picture** | **str** |  | 

## Example

```python
from gravscale.models.app_modules_authentication_schema_account_schema import AppModulesAuthenticationSchemaAccountSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AppModulesAuthenticationSchemaAccountSchema from a JSON string
app_modules_authentication_schema_account_schema_instance = AppModulesAuthenticationSchemaAccountSchema.from_json(json)
# print the JSON string representation of the object
print(AppModulesAuthenticationSchemaAccountSchema.to_json())

# convert the object into a dict
app_modules_authentication_schema_account_schema_dict = app_modules_authentication_schema_account_schema_instance.to_dict()
# create an instance of AppModulesAuthenticationSchemaAccountSchema from a dict
app_modules_authentication_schema_account_schema_from_dict = AppModulesAuthenticationSchemaAccountSchema.from_dict(app_modules_authentication_schema_account_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


