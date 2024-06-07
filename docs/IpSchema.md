# IpSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 

## Example

```python
from gravscale.models.ip_schema import IpSchema

# TODO update the JSON string below
json = "{}"
# create an instance of IpSchema from a JSON string
ip_schema_instance = IpSchema.from_json(json)
# print the JSON string representation of the object
print(IpSchema.to_json())

# convert the object into a dict
ip_schema_dict = ip_schema_instance.to_dict()
# create an instance of IpSchema from a dict
ip_schema_from_dict = IpSchema.from_dict(ip_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


