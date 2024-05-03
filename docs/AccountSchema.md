# AccountSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**email** | **str** |  | 
**nickname** | **str** |  | 
**picture** | **str** |  | 

## Example

```python
from gravscale.models.account_schema import AccountSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSchema from a JSON string
account_schema_instance = AccountSchema.from_json(json)
# print the JSON string representation of the object
print(AccountSchema.to_json())

# convert the object into a dict
account_schema_dict = account_schema_instance.to_dict()
# create an instance of AccountSchema from a dict
account_schema_from_dict = AccountSchema.from_dict(account_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


