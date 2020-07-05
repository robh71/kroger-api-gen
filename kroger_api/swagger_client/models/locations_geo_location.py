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


class LocationsGeoLocation(object):
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
        'lat_lng': 'str',
        'latitude': 'float',
        'longitude': 'float'
    }

    attribute_map = {
        'lat_lng': 'latLng',
        'latitude': 'latitude',
        'longitude': 'longitude'
    }

    def __init__(self, lat_lng=None, latitude=None, longitude=None):  # noqa: E501
        """LocationsGeoLocation - a model defined in Swagger"""  # noqa: E501
        self._lat_lng = None
        self._latitude = None
        self._longitude = None
        self.discriminator = None
        if lat_lng is not None:
            self.lat_lng = lat_lng
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude

    @property
    def lat_lng(self):
        """Gets the lat_lng of this LocationsGeoLocation.  # noqa: E501

        The latitude and longitude of the location.  # noqa: E501

        :return: The lat_lng of this LocationsGeoLocation.  # noqa: E501
        :rtype: str
        """
        return self._lat_lng

    @lat_lng.setter
    def lat_lng(self, lat_lng):
        """Sets the lat_lng of this LocationsGeoLocation.

        The latitude and longitude of the location.  # noqa: E501

        :param lat_lng: The lat_lng of this LocationsGeoLocation.  # noqa: E501
        :type: str
        """

        self._lat_lng = lat_lng

    @property
    def latitude(self):
        """Gets the latitude of this LocationsGeoLocation.  # noqa: E501

        The latitude of the location.  # noqa: E501

        :return: The latitude of this LocationsGeoLocation.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this LocationsGeoLocation.

        The latitude of the location.  # noqa: E501

        :param latitude: The latitude of this LocationsGeoLocation.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this LocationsGeoLocation.  # noqa: E501

        The longitude of the location.  # noqa: E501

        :return: The longitude of this LocationsGeoLocation.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this LocationsGeoLocation.

        The longitude of the location.  # noqa: E501

        :param longitude: The longitude of this LocationsGeoLocation.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

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
        if issubclass(LocationsGeoLocation, dict):
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
        if not isinstance(other, LocationsGeoLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other