# PageTaskTreeSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TaskTreeSchema]**](TaskTreeSchema.md) |  | 
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 

## Example

```python
from gravscale.models.page_task_tree_schema import PageTaskTreeSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PageTaskTreeSchema from a JSON string
page_task_tree_schema_instance = PageTaskTreeSchema.from_json(json)
# print the JSON string representation of the object
print(PageTaskTreeSchema.to_json())

# convert the object into a dict
page_task_tree_schema_dict = page_task_tree_schema_instance.to_dict()
# create an instance of PageTaskTreeSchema from a dict
page_task_tree_schema_from_dict = PageTaskTreeSchema.from_dict(page_task_tree_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


