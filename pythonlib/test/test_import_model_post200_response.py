# coding: utf-8

"""
    PreForm API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.import_model_post200_response import ImportModelPost200Response

class TestImportModelPost200Response(unittest.TestCase):
    """ImportModelPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportModelPost200Response:
        """Test ImportModelPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportModelPost200Response`
        """
        model = ImportModelPost200Response()
        if include_optional:
            return ImportModelPost200Response(
                model_id = ''
            )
        else:
            return ImportModelPost200Response(
        )
        """

    def testImportModelPost200Response(self):
        """Test ImportModelPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()