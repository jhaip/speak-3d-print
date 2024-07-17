# coding: utf-8

"""
    PreForm API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.printers_post200_response import PrintersPost200Response

class TestPrintersPost200Response(unittest.TestCase):
    """PrintersPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrintersPost200Response:
        """Test PrintersPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrintersPost200Response`
        """
        model = PrintersPost200Response()
        if include_optional:
            return PrintersPost200Response(
                count = 56,
                printers = [
                    openapi_client.models._printers__post_200_response_printers_inner._printers__post_200_response_printers_inner(
                        name = '', 
                        machine_type_id = '', 
                        ip_address = '', )
                    ]
            )
        else:
            return PrintersPost200Response(
        )
        """

    def testPrintersPost200Response(self):
        """Test PrintersPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()