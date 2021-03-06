# coding: utf-8

"""
    Gkeep API

    Gkeep API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class VehicleTanks(object):
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
        'id': 'int',
        'tank_type': 'VehicleTankType',
        'vehicle': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tank_type': 'tank_type',
        'vehicle': 'vehicle'
    }

    def __init__(self, id=None, tank_type=None, vehicle=None):  # noqa: E501
        """VehicleTanks - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._tank_type = None
        self._vehicle = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if tank_type is not None:
            self.tank_type = tank_type
        if vehicle is not None:
            self.vehicle = vehicle

    @property
    def id(self):
        """Gets the id of this VehicleTanks.  # noqa: E501


        :return: The id of this VehicleTanks.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VehicleTanks.


        :param id: The id of this VehicleTanks.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def tank_type(self):
        """Gets the tank_type of this VehicleTanks.  # noqa: E501


        :return: The tank_type of this VehicleTanks.  # noqa: E501
        :rtype: VehicleTankType
        """
        return self._tank_type

    @tank_type.setter
    def tank_type(self, tank_type):
        """Sets the tank_type of this VehicleTanks.


        :param tank_type: The tank_type of this VehicleTanks.  # noqa: E501
        :type: VehicleTankType
        """

        self._tank_type = tank_type

    @property
    def vehicle(self):
        """Gets the vehicle of this VehicleTanks.  # noqa: E501


        :return: The vehicle of this VehicleTanks.  # noqa: E501
        :rtype: str
        """
        return self._vehicle

    @vehicle.setter
    def vehicle(self, vehicle):
        """Sets the vehicle of this VehicleTanks.


        :param vehicle: The vehicle of this VehicleTanks.  # noqa: E501
        :type: str
        """

        self._vehicle = vehicle

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
        if issubclass(VehicleTanks, dict):
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
        if not isinstance(other, VehicleTanks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
