# ModelProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the model | [optional] 
**name** | **str** | The name of the model used within job preparation. | [optional] 
**position** | [**ScenePositionModel**](ScenePositionModel.md) |  | [optional] 
**orientation** | [**EulerAnglesModel**](EulerAnglesModel.md) |  | [optional] 
**scale** | **float** | The scale factor to apply to the model | [optional] 
**units** | [**UnitsModel**](UnitsModel.md) |  | [optional] 
**bbox** | [**ModelPropertiesBbox**](ModelPropertiesBbox.md) |  | [optional] 
**original_file** | **str** | The original file path of the model | [optional] 
**visible** | **bool** | Whether the model is visible in the scene | [optional] 
**has_supports** | **bool** | Whether the model has supports | [optional] 
**in_bounds** | **bool** | Whether the model is within the build volume | [optional] 

## Example

```python
from openapi_client.models.model_properties import ModelProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ModelProperties from a JSON string
model_properties_instance = ModelProperties.from_json(json)
# print the JSON string representation of the object
print(ModelProperties.to_json())

# convert the object into a dict
model_properties_dict = model_properties_instance.to_dict()
# create an instance of ModelProperties from a dict
model_properties_from_dict = ModelProperties.from_dict(model_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


