# coding: utf-8

"""
    Kroger API Reference

    <br> <div style=\"background-color: #ffebb2; padding: 16px; border-radius: .25rem; border: 1px solid #ff8d00; padding: 8px; font-size: 13.5px; padding-right: 12px; padding-left: 12px; padding-top: 14px; padding-bottom: 14px;\"><b>DEPRECATION NOTICE</b> - As of 06/01/2020, the Coupons API is no longer available. Currently, there is no direct replacement for the Coupons API.</div>  # Introduction The following APIs are publicly available to allow new clients to build products,  services, or customer experiences that leverage the unique data, functions, and  applications of Kroger. As a company that strives to empower the developer community  and meet our customers where they are, we are offering these APIs as the first  step to building an ecosystem that promotes speed, simplicity, and security. <br><br> To begin using our Public APIs, see the [Getting Started](https://developer.kroger.com/documentation/consume) documentation.   # Environments  During registration, we require apps to be registered for environments individually. Use one of the following paths based on the environment you selected for your application during the registration process.  | Environment | Path | |-------------|------| |Production | https://api.kroger.com/v1/ | |Certification | https://api-ce.kroger.com/v1/ |  # Authentication  For API authentication, Kroger uses the OAuth2 protocol ([RFC6749](https://tools.ietf.org/html/rfc6749)),  supporting the Authorization Code, Client Credentials, and Refresh Token grant types. If you're unfamiliar  with OAuth2, see our [Understanding OAuth2](https://developer.kroger.com/documentation/consume/guides/understanding-oauth2)  documentation.   <!-- ReDoc-Inject: <security-definitions> -->   # noqa: E501

    OpenAPI spec version: 1.2.1
    Contact: APISupport@kroger.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ClientCredentials(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'grant_type': 'str',
        'scope': 'str'
    }

    attribute_map = {
        'grant_type': 'grant_type',
        'scope': 'scope'
    }

    def __init__(self, grant_type=None, scope=None):  # noqa: E501
        """ClientCredentials - a model defined in Swagger"""  # noqa: E501
        self._grant_type = None
        self._scope = None
        self.discriminator = None
        self.grant_type = grant_type
        if scope is not None:
            self.scope = scope

    @property
    def grant_type(self):
        """Gets the grant_type of this ClientCredentials.  # noqa: E501

        Must be `client_credentials`.  # noqa: E501

        :return: The grant_type of this ClientCredentials.  # noqa: E501
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        """Sets the grant_type of this ClientCredentials.

        Must be `client_credentials`.  # noqa: E501

        :param grant_type: The grant_type of this ClientCredentials.  # noqa: E501
        :type: str
        """
        if grant_type is None:
            raise ValueError("Invalid value for `grant_type`, must not be `None`")  # noqa: E501

        self._grant_type = grant_type

    @property
    def scope(self):
        """Gets the scope of this ClientCredentials.  # noqa: E501

        The level of access your application is requesting.  # noqa: E501

        :return: The scope of this ClientCredentials.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ClientCredentials.

        The level of access your application is requesting.  # noqa: E501

        :param scope: The scope of this ClientCredentials.  # noqa: E501
        :type: str
        """
        allowed_values = ["product.compact"]  # noqa: E501
        if scope not in allowed_values:
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ClientCredentials, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClientCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
