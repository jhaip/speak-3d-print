# PrintersPost200ResponsePrintersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the printer | [optional] 
**machine_type_id** | **str** | Machine type ID of the printer | [optional] 
**ip_address** | **str** | IP address of the printer | [optional] 

## Example

```python
from openapi_client.models.printers_post200_response_printers_inner import PrintersPost200ResponsePrintersInner

# TODO update the JSON string below
json = "{}"
# create an instance of PrintersPost200ResponsePrintersInner from a JSON string
printers_post200_response_printers_inner_instance = PrintersPost200ResponsePrintersInner.from_json(json)
# print the JSON string representation of the object
print(PrintersPost200ResponsePrintersInner.to_json())

# convert the object into a dict
printers_post200_response_printers_inner_dict = printers_post200_response_printers_inner_instance.to_dict()
# create an instance of PrintersPost200ResponsePrintersInner from a dict
printers_post200_response_printers_inner_from_dict = PrintersPost200ResponsePrintersInner.from_dict(printers_post200_response_printers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


