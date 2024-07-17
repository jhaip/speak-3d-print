# OrientationModel

The orientation of the model in the scene. It can be specified using one of the following: Euler angles, a transform matrix, or direction vectors. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** | Euler angle x rotation | 
**y** | **float** | Euler angle y rotation | 
**z** | **float** | Euler angle z rotation | 
**linear** | **List[List[float]]** |  | 
**z_direction** | **List[float]** | 3D unit vector in model space saying which piece of the model will point \&quot;up\&quot; in scene space. If \&quot;X direction\&quot; is not set, X direction is chosen arbitrarily by projecting the nearest major axis to be perpendicular to Z direction.  | 
**x_direction** | **List[float]** | Optional 3D unit vector in model space, perpendicular to Z direction, saying which piece of the model will point \&quot;right\&quot; in scene space.  | [optional] 

## Example

```python
from openapi_client.models.orientation_model import OrientationModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrientationModel from a JSON string
orientation_model_instance = OrientationModel.from_json(json)
# print the JSON string representation of the object
print(OrientationModel.to_json())

# convert the object into a dict
orientation_model_dict = orientation_model_instance.to_dict()
# create an instance of OrientationModel from a dict
orientation_model_from_dict = OrientationModel.from_dict(orientation_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


