# coding: utf-8

"""
    Kroger API Reference

    <br> <div style=\"background-color: #ffebb2; padding: 16px; border-radius: .25rem; border: 1px solid #ff8d00; padding: 8px; font-size: 13.5px; padding-right: 12px; padding-left: 12px; padding-top: 14px; padding-bottom: 14px;\"><b>DEPRECATION NOTICE</b> - As of 06/01/2020, the Coupons API is no longer available. Currently, there is no direct replacement for the Coupons API.</div>  # Introduction The following APIs are publicly available to allow new clients to build products,  services, or customer experiences that leverage the unique data, functions, and  applications of Kroger. As a company that strives to empower the developer community  and meet our customers where they are, we are offering these APIs as the first  step to building an ecosystem that promotes speed, simplicity, and security. <br><br> To begin using our Public APIs, see the [Getting Started](https://developer.kroger.com/documentation/consume) documentation.   # Environments  During registration, we require apps to be registered for environments individually. Use one of the following paths based on the environment you selected for your application during the registration process.  | Environment | Path | |-------------|------| |Production | https://api.kroger.com/v1/ | |Certification | https://api-ce.kroger.com/v1/ |  # Authentication  For API authentication, Kroger uses the OAuth2 protocol ([RFC6749](https://tools.ietf.org/html/rfc6749)),  supporting the Authorization Code, Client Credentials, and Refresh Token grant types. If you're unfamiliar  with OAuth2, see our [Understanding OAuth2](https://developer.kroger.com/documentation/consume/guides/understanding-oauth2)  documentation.   <!-- ReDoc-Inject: <security-definitions> -->   # noqa: E501

    OpenAPI spec version: 1.2.1
    Contact: APISupport@kroger.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.locations_api import LocationsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestLocationsApi(unittest.TestCase):
    """LocationsApi unit test stubs"""

    def setUp(self):
        self.api = api.locations_api.LocationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_chain_exists(self):
        """Test case for chain_exists

        Chain query  # noqa: E501
        """
        pass

    def test_department_exists(self):
        """Test case for department_exists

        Department query  # noqa: E501
        """
        pass

    def test_get_chain(self):
        """Test case for get_chain

        Chain details  # noqa: E501
        """
        pass

    def test_get_department(self):
        """Test case for get_department

        Department details  # noqa: E501
        """
        pass

    def test_list_chains(self):
        """Test case for list_chains

        Chain list  # noqa: E501
        """
        pass

    def test_list_departments(self):
        """Test case for list_departments

        Department list  # noqa: E501
        """
        pass

    def test_locations_exists_by_id(self):
        """Test case for locations_exists_by_id

        Location query  # noqa: E501
        """
        pass

    def test_locations_get_by_id(self):
        """Test case for locations_get_by_id

        Location details  # noqa: E501
        """
        pass

    def test_search_locations(self):
        """Test case for search_locations

        Location list  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
