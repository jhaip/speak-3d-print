# TransformMatrixModel

Orientation specified a 3x3 matrix, the linear component of a 3D rigid transform.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linear** | **List[List[float]]** |  | 

## Example

```python
from formlabs.models.transform_matrix_model import TransformMatrixModel

# TODO update the JSON string below
json = "{}"
# create an instance of TransformMatrixModel from a JSON string
transform_matrix_model_instance = TransformMatrixModel.from_json(json)
# print the JSON string representation of the object
print(TransformMatrixModel.to_json())

# convert the object into a dict
transform_matrix_model_dict = transform_matrix_model_instance.to_dict()
# create an instance of TransformMatrixModel from a dict
transform_matrix_model_from_dict = TransformMatrixModel.from_dict(transform_matrix_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


