# TaskSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | **str** |  | 
**error** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from gravscale.models.task_schema import TaskSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TaskSchema from a JSON string
task_schema_instance = TaskSchema.from_json(json)
# print the JSON string representation of the object
print(TaskSchema.to_json())

# convert the object into a dict
task_schema_dict = task_schema_instance.to_dict()
# create an instance of TaskSchema from a dict
task_schema_from_dict = TaskSchema.from_dict(task_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


