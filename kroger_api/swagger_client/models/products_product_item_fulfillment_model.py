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


class ProductsProductItemFulfillmentModel(object):
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
        'curbside': 'bool',
        'delivery': 'bool',
        'instore': 'bool',
        'shiptohome': 'bool'
    }

    attribute_map = {
        'curbside': 'curbside',
        'delivery': 'delivery',
        'instore': 'instore',
        'shiptohome': 'shiptohome'
    }

    def __init__(self, curbside=None, delivery=None, instore=None, shiptohome=None):  # noqa: E501
        """ProductsProductItemFulfillmentModel - a model defined in Swagger"""  # noqa: E501
        self._curbside = None
        self._delivery = None
        self._instore = None
        self._shiptohome = None
        self.discriminator = None
        if curbside is not None:
            self.curbside = curbside
        if delivery is not None:
            self.delivery = delivery
        if instore is not None:
            self.instore = instore
        if shiptohome is not None:
            self.shiptohome = shiptohome

    @property
    def curbside(self):
        """Gets the curbside of this ProductsProductItemFulfillmentModel.  # noqa: E501

        Indicates if the product is available for curbside pickup.  # noqa: E501

        :return: The curbside of this ProductsProductItemFulfillmentModel.  # noqa: E501
        :rtype: bool
        """
        return self._curbside

    @curbside.setter
    def curbside(self, curbside):
        """Sets the curbside of this ProductsProductItemFulfillmentModel.

        Indicates if the product is available for curbside pickup.  # noqa: E501

        :param curbside: The curbside of this ProductsProductItemFulfillmentModel.  # noqa: E501
        :type: bool
        """

        self._curbside = curbside

    @property
    def delivery(self):
        """Gets the delivery of this ProductsProductItemFulfillmentModel.  # noqa: E501

        Indicates if the product is available for home delivery.  # noqa: E501

        :return: The delivery of this ProductsProductItemFulfillmentModel.  # noqa: E501
        :rtype: bool
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """Sets the delivery of this ProductsProductItemFulfillmentModel.

        Indicates if the product is available for home delivery.  # noqa: E501

        :param delivery: The delivery of this ProductsProductItemFulfillmentModel.  # noqa: E501
        :type: bool
        """

        self._delivery = delivery

    @property
    def instore(self):
        """Gets the instore of this ProductsProductItemFulfillmentModel.  # noqa: E501

        Indicates if the product is available in store. This does not indicate that the item is in stock.  # noqa: E501

        :return: The instore of this ProductsProductItemFulfillmentModel.  # noqa: E501
        :rtype: bool
        """
        return self._instore

    @instore.setter
    def instore(self, instore):
        """Sets the instore of this ProductsProductItemFulfillmentModel.

        Indicates if the product is available in store. This does not indicate that the item is in stock.  # noqa: E501

        :param instore: The instore of this ProductsProductItemFulfillmentModel.  # noqa: E501
        :type: bool
        """

        self._instore = instore

    @property
    def shiptohome(self):
        """Gets the shiptohome of this ProductsProductItemFulfillmentModel.  # noqa: E501

        Indicates if the product is available to be shipped from a fulfillment center.  # noqa: E501

        :return: The shiptohome of this ProductsProductItemFulfillmentModel.  # noqa: E501
        :rtype: bool
        """
        return self._shiptohome

    @shiptohome.setter
    def shiptohome(self, shiptohome):
        """Sets the shiptohome of this ProductsProductItemFulfillmentModel.

        Indicates if the product is available to be shipped from a fulfillment center.  # noqa: E501

        :param shiptohome: The shiptohome of this ProductsProductItemFulfillmentModel.  # noqa: E501
        :type: bool
        """

        self._shiptohome = shiptohome

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
        if issubclass(ProductsProductItemFulfillmentModel, dict):
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
        if not isinstance(other, ProductsProductItemFulfillmentModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other