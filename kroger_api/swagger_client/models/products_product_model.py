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


class ProductsProductModel(object):
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
        'product_id': 'str',
        'aisle_locations': 'list[ProductsProductAisleLocationModel]',
        'brand': 'str',
        'categories': 'list[str]',
        'country_origin': 'str',
        'description': 'str',
        'items': 'list[ProductsProductItemModel]',
        'item_information': 'ProductsProductBoxedDimensionsModel',
        'temperature': 'ProductsProductTemperatureModel',
        'images': 'list[ProductsProductImageModel]',
        'upc': 'str'
    }

    attribute_map = {
        'product_id': 'productId',
        'aisle_locations': 'aisleLocations',
        'brand': 'brand',
        'categories': 'categories',
        'country_origin': 'countryOrigin',
        'description': 'description',
        'items': 'items',
        'item_information': 'itemInformation',
        'temperature': 'temperature',
        'images': 'images',
        'upc': 'upc'
    }

    def __init__(self, product_id=None, aisle_locations=None, brand=None, categories=None, country_origin=None, description=None, items=None, item_information=None, temperature=None, images=None, upc=None):  # noqa: E501
        """ProductsProductModel - a model defined in Swagger"""  # noqa: E501
        self._product_id = None
        self._aisle_locations = None
        self._brand = None
        self._categories = None
        self._country_origin = None
        self._description = None
        self._items = None
        self._item_information = None
        self._temperature = None
        self._images = None
        self._upc = None
        self.discriminator = None
        if product_id is not None:
            self.product_id = product_id
        if aisle_locations is not None:
            self.aisle_locations = aisle_locations
        if brand is not None:
            self.brand = brand
        if categories is not None:
            self.categories = categories
        if country_origin is not None:
            self.country_origin = country_origin
        if description is not None:
            self.description = description
        if items is not None:
            self.items = items
        if item_information is not None:
            self.item_information = item_information
        if temperature is not None:
            self.temperature = temperature
        if images is not None:
            self.images = images
        if upc is not None:
            self.upc = upc

    @property
    def product_id(self):
        """Gets the product_id of this ProductsProductModel.  # noqa: E501

        The UPC of the product.  # noqa: E501

        :return: The product_id of this ProductsProductModel.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ProductsProductModel.

        The UPC of the product.  # noqa: E501

        :param product_id: The product_id of this ProductsProductModel.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def aisle_locations(self):
        """Gets the aisle_locations of this ProductsProductModel.  # noqa: E501


        :return: The aisle_locations of this ProductsProductModel.  # noqa: E501
        :rtype: list[ProductsProductAisleLocationModel]
        """
        return self._aisle_locations

    @aisle_locations.setter
    def aisle_locations(self, aisle_locations):
        """Sets the aisle_locations of this ProductsProductModel.


        :param aisle_locations: The aisle_locations of this ProductsProductModel.  # noqa: E501
        :type: list[ProductsProductAisleLocationModel]
        """

        self._aisle_locations = aisle_locations

    @property
    def brand(self):
        """Gets the brand of this ProductsProductModel.  # noqa: E501

        The brand name of the product.  # noqa: E501

        :return: The brand of this ProductsProductModel.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this ProductsProductModel.

        The brand name of the product.  # noqa: E501

        :param brand: The brand of this ProductsProductModel.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def categories(self):
        """Gets the categories of this ProductsProductModel.  # noqa: E501

        The category the product belongs to.  # noqa: E501

        :return: The categories of this ProductsProductModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this ProductsProductModel.

        The category the product belongs to.  # noqa: E501

        :param categories: The categories of this ProductsProductModel.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def country_origin(self):
        """Gets the country_origin of this ProductsProductModel.  # noqa: E501

        The country of origin of the product.  # noqa: E501

        :return: The country_origin of this ProductsProductModel.  # noqa: E501
        :rtype: str
        """
        return self._country_origin

    @country_origin.setter
    def country_origin(self, country_origin):
        """Sets the country_origin of this ProductsProductModel.

        The country of origin of the product.  # noqa: E501

        :param country_origin: The country_origin of this ProductsProductModel.  # noqa: E501
        :type: str
        """

        self._country_origin = country_origin

    @property
    def description(self):
        """Gets the description of this ProductsProductModel.  # noqa: E501

        The name of the product.  # noqa: E501

        :return: The description of this ProductsProductModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProductsProductModel.

        The name of the product.  # noqa: E501

        :param description: The description of this ProductsProductModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def items(self):
        """Gets the items of this ProductsProductModel.  # noqa: E501


        :return: The items of this ProductsProductModel.  # noqa: E501
        :rtype: list[ProductsProductItemModel]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ProductsProductModel.


        :param items: The items of this ProductsProductModel.  # noqa: E501
        :type: list[ProductsProductItemModel]
        """

        self._items = items

    @property
    def item_information(self):
        """Gets the item_information of this ProductsProductModel.  # noqa: E501


        :return: The item_information of this ProductsProductModel.  # noqa: E501
        :rtype: ProductsProductBoxedDimensionsModel
        """
        return self._item_information

    @item_information.setter
    def item_information(self, item_information):
        """Sets the item_information of this ProductsProductModel.


        :param item_information: The item_information of this ProductsProductModel.  # noqa: E501
        :type: ProductsProductBoxedDimensionsModel
        """

        self._item_information = item_information

    @property
    def temperature(self):
        """Gets the temperature of this ProductsProductModel.  # noqa: E501


        :return: The temperature of this ProductsProductModel.  # noqa: E501
        :rtype: ProductsProductTemperatureModel
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this ProductsProductModel.


        :param temperature: The temperature of this ProductsProductModel.  # noqa: E501
        :type: ProductsProductTemperatureModel
        """

        self._temperature = temperature

    @property
    def images(self):
        """Gets the images of this ProductsProductModel.  # noqa: E501


        :return: The images of this ProductsProductModel.  # noqa: E501
        :rtype: list[ProductsProductImageModel]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this ProductsProductModel.


        :param images: The images of this ProductsProductModel.  # noqa: E501
        :type: list[ProductsProductImageModel]
        """

        self._images = images

    @property
    def upc(self):
        """Gets the upc of this ProductsProductModel.  # noqa: E501

        The UPC of the product  # noqa: E501

        :return: The upc of this ProductsProductModel.  # noqa: E501
        :rtype: str
        """
        return self._upc

    @upc.setter
    def upc(self, upc):
        """Sets the upc of this ProductsProductModel.

        The UPC of the product  # noqa: E501

        :param upc: The upc of this ProductsProductModel.  # noqa: E501
        :type: str
        """

        self._upc = upc

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
        if issubclass(ProductsProductModel, dict):
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
        if not isinstance(other, ProductsProductModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
