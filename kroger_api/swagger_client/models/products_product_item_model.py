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


class ProductsProductItemModel(object):
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
        'item_id': 'str',
        'favorite': 'bool',
        'fulfillment': 'ProductsProductItemFulfillmentModel',
        'price': 'ProductsProductItemPriceModel',
        'national_price': 'ProductsProductItemPriceModel',
        'size': 'str',
        'sold_by': 'str'
    }

    attribute_map = {
        'item_id': 'itemId',
        'favorite': 'favorite',
        'fulfillment': 'fulfillment',
        'price': 'price',
        'national_price': 'nationalPrice',
        'size': 'size',
        'sold_by': 'soldBy'
    }

    def __init__(self, item_id=None, favorite=None, fulfillment=None, price=None, national_price=None, size=None, sold_by=None):  # noqa: E501
        """ProductsProductItemModel - a model defined in Swagger"""  # noqa: E501
        self._item_id = None
        self._favorite = None
        self._fulfillment = None
        self._price = None
        self._national_price = None
        self._size = None
        self._sold_by = None
        self.discriminator = None
        if item_id is not None:
            self.item_id = item_id
        if favorite is not None:
            self.favorite = favorite
        if fulfillment is not None:
            self.fulfillment = fulfillment
        if price is not None:
            self.price = price
        if national_price is not None:
            self.national_price = national_price
        if size is not None:
            self.size = size
        if sold_by is not None:
            self.sold_by = sold_by

    @property
    def item_id(self):
        """Gets the item_id of this ProductsProductItemModel.  # noqa: E501

        The UPC of the product.  # noqa: E501

        :return: The item_id of this ProductsProductItemModel.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this ProductsProductItemModel.

        The UPC of the product.  # noqa: E501

        :param item_id: The item_id of this ProductsProductItemModel.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def favorite(self):
        """Gets the favorite of this ProductsProductItemModel.  # noqa: E501


        :return: The favorite of this ProductsProductItemModel.  # noqa: E501
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this ProductsProductItemModel.


        :param favorite: The favorite of this ProductsProductItemModel.  # noqa: E501
        :type: bool
        """

        self._favorite = favorite

    @property
    def fulfillment(self):
        """Gets the fulfillment of this ProductsProductItemModel.  # noqa: E501


        :return: The fulfillment of this ProductsProductItemModel.  # noqa: E501
        :rtype: ProductsProductItemFulfillmentModel
        """
        return self._fulfillment

    @fulfillment.setter
    def fulfillment(self, fulfillment):
        """Sets the fulfillment of this ProductsProductItemModel.


        :param fulfillment: The fulfillment of this ProductsProductItemModel.  # noqa: E501
        :type: ProductsProductItemFulfillmentModel
        """

        self._fulfillment = fulfillment

    @property
    def price(self):
        """Gets the price of this ProductsProductItemModel.  # noqa: E501


        :return: The price of this ProductsProductItemModel.  # noqa: E501
        :rtype: ProductsProductItemPriceModel
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ProductsProductItemModel.


        :param price: The price of this ProductsProductItemModel.  # noqa: E501
        :type: ProductsProductItemPriceModel
        """

        self._price = price

    @property
    def national_price(self):
        """Gets the national_price of this ProductsProductItemModel.  # noqa: E501


        :return: The national_price of this ProductsProductItemModel.  # noqa: E501
        :rtype: ProductsProductItemPriceModel
        """
        return self._national_price

    @national_price.setter
    def national_price(self, national_price):
        """Sets the national_price of this ProductsProductItemModel.


        :param national_price: The national_price of this ProductsProductItemModel.  # noqa: E501
        :type: ProductsProductItemPriceModel
        """

        self._national_price = national_price

    @property
    def size(self):
        """Gets the size of this ProductsProductItemModel.  # noqa: E501

        A description of product's size.  # noqa: E501

        :return: The size of this ProductsProductItemModel.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ProductsProductItemModel.

        A description of product's size.  # noqa: E501

        :param size: The size of this ProductsProductItemModel.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def sold_by(self):
        """Gets the sold_by of this ProductsProductItemModel.  # noqa: E501

        Indicates how this item is sold. Values returned are typically either \"weight\" or \"unit\"  # noqa: E501

        :return: The sold_by of this ProductsProductItemModel.  # noqa: E501
        :rtype: str
        """
        return self._sold_by

    @sold_by.setter
    def sold_by(self, sold_by):
        """Sets the sold_by of this ProductsProductItemModel.

        Indicates how this item is sold. Values returned are typically either \"weight\" or \"unit\"  # noqa: E501

        :param sold_by: The sold_by of this ProductsProductItemModel.  # noqa: E501
        :type: str
        """

        self._sold_by = sold_by

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
        if issubclass(ProductsProductItemModel, dict):
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
        if not isinstance(other, ProductsProductItemModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
