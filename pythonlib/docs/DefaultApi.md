# formlabs.DefaultApi

All URIs are relative to *http://localhost:44388*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auto_layout_post**](DefaultApi.md#auto_layout_post) | **POST** /auto-layout/ | 
[**auto_orient_post**](DefaultApi.md#auto_orient_post) | **POST** /auto-orient/ | 
[**auto_support_post**](DefaultApi.md#auto_support_post) | **POST** /auto-support/ | 
[**export_post**](DefaultApi.md#export_post) | **POST** /export/ | 
[**load_form_post**](DefaultApi.md#load_form_post) | **POST** /load-form/ | 
[**models_id_delete**](DefaultApi.md#models_id_delete) | **DELETE** /models/{id}/ | 
[**save_form_post**](DefaultApi.md#save_form_post) | **POST** /save-form/ | 
[**scene_get**](DefaultApi.md#scene_get) | **GET** /scene | 
[**scene_import_model_post**](DefaultApi.md#scene_import_model_post) | **POST** /scene/import-model/ | 
[**scene_post**](DefaultApi.md#scene_post) | **POST** /scene | 
[**v1_print_post**](DefaultApi.md#v1_print_post) | **POST** /v1/print/ | 
[**v1_slice_post**](DefaultApi.md#v1_slice_post) | **POST** /v1/slice/ | 


# **auto_layout_post**
> auto_layout_post(auto_orient_post_request)



Run auto layout operation

### Example


```python
import formlabs
from formlabs.models.auto_orient_post_request import AutoOrientPostRequest
from formlabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs.DefaultApi(api_client)
    auto_orient_post_request = {"models":"ALL"} # AutoOrientPostRequest | Models to run the auto layout operation on

    try:
        api_instance.auto_layout_post(auto_orient_post_request)
    except Exception as e:
        print("Exception when calling DefaultApi->auto_layout_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_orient_post_request** | [**AutoOrientPostRequest**](AutoOrientPostRequest.md)| Models to run the auto layout operation on | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Operation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auto_orient_post**
> auto_orient_post(auto_orient_post_request)



Run auto orient operation

### Example


```python
import formlabs
from formlabs.models.auto_orient_post_request import AutoOrientPostRequest
from formlabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs.DefaultApi(api_client)
    auto_orient_post_request = {"models":"ALL"} # AutoOrientPostRequest | Models to run the auto orient operation on

    try:
        api_instance.auto_orient_post(auto_orient_post_request)
    except Exception as e:
        print("Exception when calling DefaultApi->auto_orient_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_orient_post_request** | [**AutoOrientPostRequest**](AutoOrientPostRequest.md)| Models to run the auto orient operation on | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auto_support_post**
> auto_support_post(auto_orient_post_request)



Run auto support operation

### Example


```python
import formlabs
from formlabs.models.auto_orient_post_request import AutoOrientPostRequest
from formlabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs.DefaultApi(api_client)
    auto_orient_post_request = {"models":"ALL"} # AutoOrientPostRequest | Models to run the auto support operation on

    try:
        api_instance.auto_support_post(auto_orient_post_request)
    except Exception as e:
        print("Exception when calling DefaultApi->auto_support_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_orient_post_request** | [**AutoOrientPostRequest**](AutoOrientPostRequest.md)| Models to run the auto support operation on | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_post**
> ExportPost200Response export_post(output_path)



Export current scene as a STL

### Example


```python
import formlabs
from formlabs.models.export_post200_response import ExportPost200Response
from formlabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs.DefaultApi(api_client)
    output_path = 'output_path_example' # str | The path to the output file where the .STL will be saved

    try:
        api_response = api_instance.export_post(output_path)
        print("The response of DefaultApi->export_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->export_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_path** | **str**| The path to the output file where the .STL will be saved | 

### Return type

[**ExportPost200Response**](ExportPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_form_post**
> load_form_post(file)



Load a file into the current scene

### Example


```python
import formlabs
from formlabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs.DefaultApi(api_client)
    file = 'file_example' # str | 

    try:
        api_instance.load_form_post(file)
    except Exception as e:
        print("Exception when calling DefaultApi->load_form_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_id_delete**
> models_id_delete(id)



Delete a model into the current scene

### Example


```python
import formlabs
from formlabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs.DefaultApi(api_client)
    id = 'id_example' # str | The unique identifier of the model

    try:
        api_instance.models_id_delete(id)
    except Exception as e:
        print("Exception when calling DefaultApi->models_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the model | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_form_post**
> save_form_post(file)



Save the current scene to a .FORM file

### Example


```python
import formlabs
from formlabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs.DefaultApi(api_client)
    file = 'file_example' # str | 

    try:
        api_instance.save_form_post(file)
    except Exception as e:
        print("Exception when calling DefaultApi->save_form_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scene_get**
> Dict[str, object] scene_get()



### Example


```python
import formlabs
from formlabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs.DefaultApi(api_client)

    try:
        api_response = api_instance.scene_get()
        print("The response of DefaultApi->scene_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->scene_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scene description |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scene_import_model_post**
> SceneImportModelPost200Response scene_import_model_post(scene_import_model_post_request)



Load a model into the current scene

### Example


```python
import formlabs
from formlabs.models.scene_import_model_post200_response import SceneImportModelPost200Response
from formlabs.models.scene_import_model_post_request import SceneImportModelPostRequest
from formlabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs.DefaultApi(api_client)
    scene_import_model_post_request = {"file":"C:\\Users\\user\\Desktop\\test.stl"} # SceneImportModelPostRequest | 

    try:
        api_response = api_instance.scene_import_model_post(scene_import_model_post_request)
        print("The response of DefaultApi->scene_import_model_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->scene_import_model_post: %s\n" % e)
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

# **scene_post**
> scene_post(scene_post_request)



Create a new scene

### Example


```python
import formlabs
from formlabs.models.scene_post_request import ScenePostRequest
from formlabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs.DefaultApi(api_client)
    scene_post_request = {"machineType":"PILK-1-0","materialCode":"FLP11B01","printSetting":"DEFAULT","sliceThickness":0.11} # ScenePostRequest | Machine type and material type selection

    try:
        api_instance.scene_post(scene_post_request)
    except Exception as e:
        print("Exception when calling DefaultApi->scene_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_post_request** | [**ScenePostRequest**](ScenePostRequest.md)| Machine type and material type selection | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_print_post**
> V1PrintPost200Response v1_print_post(printer, job_name)



Send the current scene to the printer

### Example


```python
import formlabs
from formlabs.models.v1_print_post200_response import V1PrintPost200Response
from formlabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs.DefaultApi(api_client)
    printer = 'printer_example' # str | 
    job_name = 'job_name_example' # str | 

    try:
        api_response = api_instance.v1_print_post(printer, job_name)
        print("The response of DefaultApi->v1_print_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_print_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **printer** | **str**|  | 
 **job_name** | **str**|  | 

### Return type

[**V1PrintPost200Response**](V1PrintPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_slice_post**
> v1_slice_post(file, job_name)



Slice the current scene

### Example


```python
import formlabs
from formlabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs.DefaultApi(api_client)
    file = 'file_example' # str | 
    job_name = 'job_name_example' # str | 

    try:
        api_instance.v1_slice_post(file, job_name)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_slice_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **job_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

