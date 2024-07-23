# EulerAnglesModel

Orientation specified using Euler angles in radians. TODO applied in what order, in which direction? What axis has worst gimbal lock?

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** | Euler angle x rotation | 
**y** | **float** | Euler angle y rotation | 
**z** | **float** | Euler angle z rotation | 

## Example

```python
from formlabs.models.euler_angles_model import EulerAnglesModel

# TODO update the JSON string below
json = "{}"
# create an instance of EulerAnglesModel from a JSON string
euler_angles_model_instance = EulerAnglesModel.from_json(json)
# print the JSON string representation of the object
print(EulerAnglesModel.to_json())

# convert the object into a dict
euler_angles_model_dict = euler_angles_model_instance.to_dict()
# create an instance of EulerAnglesModel from a dict
euler_angles_model_from_dict = EulerAnglesModel.from_dict(euler_angles_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


