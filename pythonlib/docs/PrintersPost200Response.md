# PrintersPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of discovered printers | [optional] 
**printers** | [**List[PrintersPost200ResponsePrintersInner]**](PrintersPost200ResponsePrintersInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.printers_post200_response import PrintersPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrintersPost200Response from a JSON string
printers_post200_response_instance = PrintersPost200Response.from_json(json)
# print the JSON string representation of the object
print(PrintersPost200Response.to_json())

# convert the object into a dict
printers_post200_response_dict = printers_post200_response_instance.to_dict()
# create an instance of PrintersPost200Response from a dict
printers_post200_response_from_dict = PrintersPost200Response.from_dict(printers_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


