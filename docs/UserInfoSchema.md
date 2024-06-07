# UserInfoSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**nickname** | **str** |  | 

## Example

```python
from gravscale.models.user_info_schema import UserInfoSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UserInfoSchema from a JSON string
user_info_schema_instance = UserInfoSchema.from_json(json)
# print the JSON string representation of the object
print(UserInfoSchema.to_json())

# convert the object into a dict
user_info_schema_dict = user_info_schema_instance.to_dict()
# create an instance of UserInfoSchema from a dict
user_info_schema_from_dict = UserInfoSchema.from_dict(user_info_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


