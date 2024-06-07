# GroupSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from gravscale.models.group_schema import GroupSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSchema from a JSON string
group_schema_instance = GroupSchema.from_json(json)
# print the JSON string representation of the object
print(GroupSchema.to_json())

# convert the object into a dict
group_schema_dict = group_schema_instance.to_dict()
# create an instance of GroupSchema from a dict
group_schema_from_dict = GroupSchema.from_dict(group_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


