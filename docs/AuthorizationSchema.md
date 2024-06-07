# AuthorizationSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**refresh_token** | **str** |  | [optional] 
**type** | **str** |  | 
**expires_at** | **datetime** |  | 

## Example

```python
from gravscale.models.authorization_schema import AuthorizationSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationSchema from a JSON string
authorization_schema_instance = AuthorizationSchema.from_json(json)
# print the JSON string representation of the object
print(AuthorizationSchema.to_json())

# convert the object into a dict
authorization_schema_dict = authorization_schema_instance.to_dict()
# create an instance of AuthorizationSchema from a dict
authorization_schema_from_dict = AuthorizationSchema.from_dict(authorization_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


