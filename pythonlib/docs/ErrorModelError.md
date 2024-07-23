# ErrorModelError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Unique and stable string identifying this error, e.g. \&quot;PRINTER_IP_NOT_FOUND\&quot; | [optional] 
**message** | **str** | Human-readable english string describing the error, e.g. \&quot;The printer at IP address 10.34.0.1 could not be found\&quot; | [optional] 

## Example

```python
from formlabs.models.error_model_error import ErrorModelError

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorModelError from a JSON string
error_model_error_instance = ErrorModelError.from_json(json)
# print the JSON string representation of the object
print(ErrorModelError.to_json())

# convert the object into a dict
error_model_error_dict = error_model_error_instance.to_dict()
# create an instance of ErrorModelError from a dict
error_model_error_from_dict = ErrorModelError.from_dict(error_model_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


