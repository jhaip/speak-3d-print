# coding: utf-8

"""
    PreForm API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.model_properties_bbox import ModelPropertiesBbox

class TestModelPropertiesBbox(unittest.TestCase):
    """ModelPropertiesBbox unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModelPropertiesBbox:
        """Test ModelPropertiesBbox
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModelPropertiesBbox`
        """
        model = ModelPropertiesBbox()
        if include_optional:
            return ModelPropertiesBbox(
                min_corner = openapi_client.models.scene_position_model.ScenePositionModel(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ),
                max_corner = openapi_client.models.scene_position_model.ScenePositionModel(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, )
            )
        else:
            return ModelPropertiesBbox(
        )
        """

    def testModelPropertiesBbox(self):
        """Test ModelPropertiesBbox"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()