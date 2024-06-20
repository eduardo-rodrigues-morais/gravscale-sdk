# TaskTreeSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | **str** |  | 
**action** | **str** |  | [optional] 
**result** | **object** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**client_id** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**percentage_complete** | **int** |  | [optional] [default to 0]
**sub_tasks** | [**List[TaskSchema]**](TaskSchema.md) |  | [optional] 

## Example

```python
from gravscale.models.task_tree_schema import TaskTreeSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTreeSchema from a JSON string
task_tree_schema_instance = TaskTreeSchema.from_json(json)
# print the JSON string representation of the object
print(TaskTreeSchema.to_json())

# convert the object into a dict
task_tree_schema_dict = task_tree_schema_instance.to_dict()
# create an instance of TaskTreeSchema from a dict
task_tree_schema_from_dict = TaskTreeSchema.from_dict(task_tree_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


