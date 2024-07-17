# ScenePositionModel

The global position within the build volume of a printer of the model in the scene

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** | X-position, with 0 at the center of the print volume, and positive values moving to the right as you face the printer. | [optional] 
**y** | **float** | Y-position, with 0 at the center of the print volume and positive values moving away from you as you face the printer. | [optional] 
**z** | **float** | Vertical position of the model, with 0 at the bottom of the build platform. | [optional] 

## Example

```python
from openapi_client.models.scene_position_model import ScenePositionModel

# TODO update the JSON string below
json = "{}"
# create an instance of ScenePositionModel from a JSON string
scene_position_model_instance = ScenePositionModel.from_json(json)
# print the JSON string representation of the object
print(ScenePositionModel.to_json())

# convert the object into a dict
scene_position_model_dict = scene_position_model_instance.to_dict()
# create an instance of ScenePositionModel from a dict
scene_position_model_from_dict = ScenePositionModel.from_dict(scene_position_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


