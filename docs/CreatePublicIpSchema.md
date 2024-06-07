# CreatePublicIpSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpc_name** | **str** |  | 
**address** | **str** |  | 

## Example

```python
from gravscale.models.create_public_ip_schema import CreatePublicIpSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePublicIpSchema from a JSON string
create_public_ip_schema_instance = CreatePublicIpSchema.from_json(json)
# print the JSON string representation of the object
print(CreatePublicIpSchema.to_json())

# convert the object into a dict
create_public_ip_schema_dict = create_public_ip_schema_instance.to_dict()
# create an instance of CreatePublicIpSchema from a dict
create_public_ip_schema_from_dict = CreatePublicIpSchema.from_dict(create_public_ip_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


