# SceneImportModelPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** | Full path to the file to load | 
**repair_behavior** | [**RepairBehaviorModel**](RepairBehaviorModel.md) |  | [optional] 
**name** | **str** | The name of the model used within job preparation. | [optional] 
**position** | [**ScenePositionModel**](ScenePositionModel.md) |  | [optional] 
**orientation** | [**OrientationModel**](OrientationModel.md) |  | [optional] 
**scale** | **float** | The scale factor to apply to the model | [optional] [default to 1]
**units** | [**ImportUnitsModel**](ImportUnitsModel.md) |  | [optional] 

## Example

```python
from formlabs.models.scene_import_model_post_request import SceneImportModelPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SceneImportModelPostRequest from a JSON string
scene_import_model_post_request_instance = SceneImportModelPostRequest.from_json(json)
# print the JSON string representation of the object
print(SceneImportModelPostRequest.to_json())

# convert the object into a dict
scene_import_model_post_request_dict = scene_import_model_post_request_instance.to_dict()
# create an instance of SceneImportModelPostRequest from a dict
scene_import_model_post_request_from_dict = SceneImportModelPostRequest.from_dict(scene_import_model_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


