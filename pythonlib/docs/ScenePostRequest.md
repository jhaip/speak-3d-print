# ScenePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_type** | **str** |  | 
**material_code** | **str** |  | 
**print_setting** | **str** |  | 
**slice_thickness** | **float** |  | 

## Example

```python
from formlabs.models.scene_post_request import ScenePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScenePostRequest from a JSON string
scene_post_request_instance = ScenePostRequest.from_json(json)
# print the JSON string representation of the object
print(ScenePostRequest.to_json())

# convert the object into a dict
scene_post_request_dict = scene_post_request_instance.to_dict()
# create an instance of ScenePostRequest from a dict
scene_post_request_from_dict = ScenePostRequest.from_dict(scene_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


