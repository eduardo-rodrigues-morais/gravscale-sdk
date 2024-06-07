# AppModulesAccountSchemaAccountSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**client_id** | **int** |  | 
**client_status** | **str** |  | 

## Example

```python
from gravscale.models.app_modules_account_schema_account_schema import AppModulesAccountSchemaAccountSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AppModulesAccountSchemaAccountSchema from a JSON string
app_modules_account_schema_account_schema_instance = AppModulesAccountSchemaAccountSchema.from_json(json)
# print the JSON string representation of the object
print(AppModulesAccountSchemaAccountSchema.to_json())

# convert the object into a dict
app_modules_account_schema_account_schema_dict = app_modules_account_schema_account_schema_instance.to_dict()
# create an instance of AppModulesAccountSchemaAccountSchema from a dict
app_modules_account_schema_account_schema_from_dict = AppModulesAccountSchemaAccountSchema.from_dict(app_modules_account_schema_account_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


