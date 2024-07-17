# coding: utf-8

"""
    PreForm API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.orientation_model import OrientationModel

class TestOrientationModel(unittest.TestCase):
    """OrientationModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrientationModel:
        """Test OrientationModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrientationModel`
        """
        model = OrientationModel()
        if include_optional:
            return OrientationModel(
                x = 1.337,
                y = 1.337,
                z = 1.337,
                linear = [
                    [
                        1.337
                        ]
                    ],
                z_direction = [
                    1.337
                    ],
                x_direction = [
                    1.337
                    ]
            )
        else:
            return OrientationModel(
                x = 1.337,
                y = 1.337,
                z = 1.337,
                linear = [
                    [
                        1.337
                        ]
                    ],
                z_direction = [
                    1.337
                    ],
        )
        """

    def testOrientationModel(self):
        """Test OrientationModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()