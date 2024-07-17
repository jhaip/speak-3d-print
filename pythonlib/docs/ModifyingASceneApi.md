# openapi_client.ModifyingASceneApi

All URIs are relative to *http://localhost:44388*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scene_import_model_post**](ModifyingASceneApi.md#scene_import_model_post) | **POST** /scene/import-model/ | 


# **scene_import_model_post**
> SceneImportModelPost200Response scene_import_model_post(scene_import_model_post_request)



Load a model into the current scene

### Example


```python
import openapi_client
from openapi_client.models.scene_import_model_post200_response import SceneImportModelPost200Response
from openapi_client.models.scene_import_model_post_request import SceneImportModelPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ModifyingASceneApi(api_client)
    scene_import_model_post_request = {"file":"C:\\Users\\user\\Desktop\\test.stl"} # SceneImportModelPostRequest | 

    try:
        api_response = api_instance.scene_import_model_post(scene_import_model_post_request)
        print("The response of ModifyingASceneApi->scene_import_model_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModifyingASceneApi->scene_import_model_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_import_model_post_request** | [**SceneImportModelPostRequest**](SceneImportModelPostRequest.md)|  | 

### Return type

[**SceneImportModelPost200Response**](SceneImportModelPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

