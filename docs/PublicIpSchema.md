# PublicIpSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**vpc** | [**AppModulesNetworkSchemaVpcSchema**](AppModulesNetworkSchemaVpcSchema.md) |  | 
**public_ip** | [**List[IpSchema]**](IpSchema.md) |  | 

## Example

```python
from gravscale.models.public_ip_schema import PublicIpSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PublicIpSchema from a JSON string
public_ip_schema_instance = PublicIpSchema.from_json(json)
# print the JSON string representation of the object
print(PublicIpSchema.to_json())

# convert the object into a dict
public_ip_schema_dict = public_ip_schema_instance.to_dict()
# create an instance of PublicIpSchema from a dict
public_ip_schema_from_dict = PublicIpSchema.from_dict(public_ip_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


