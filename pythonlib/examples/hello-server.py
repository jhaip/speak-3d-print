import openapi_client
import formlabs
from openapi_client.rest import ApiException
from pprint import pprint

def hello_server():
     with formlabs.PreFormApi.start_preform_server() as preform:
        try:
            preform.api.scene_post({
                "machine_type": "FORM-4-0",
                "material_code": "FLRG1011",
                "slice_thickness": 0.1,
                "print_setting": "DEFAULT",
            })
        except ApiException as e:
            print("Exception when calling DefaultApi->auto_layout_post: %s\n" % e)

        print("Scene created")

if (__name__ == "__main__"):
    hello_server()
