# ModelPropertiesBbox


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_corner** | [**ScenePositionModel**](ScenePositionModel.md) |  | [optional] 
**max_corner** | [**ScenePositionModel**](ScenePositionModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.model_properties_bbox import ModelPropertiesBbox

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPropertiesBbox from a JSON string
model_properties_bbox_instance = ModelPropertiesBbox.from_json(json)
# print the JSON string representation of the object
print(ModelPropertiesBbox.to_json())

# convert the object into a dict
model_properties_bbox_dict = model_properties_bbox_instance.to_dict()
# create an instance of ModelPropertiesBbox from a dict
model_properties_bbox_from_dict = ModelPropertiesBbox.from_dict(model_properties_bbox_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


