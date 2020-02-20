# coding: utf-8

"""
    Gkeep API

    Gkeep API  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class CreateProfileUserNavSystemAccessData(object):
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
        'account': 'str',
        'password': 'str',
        'username': 'str',
        'apikey': 'str'
    }

    attribute_map = {
        'account': 'account',
        'password': 'password',
        'username': 'username',
        'apikey': 'apikey'
    }

    def __init__(self, account=None, password=None, username=None, apikey=None):  # noqa: E501
        """CreateProfileUserNavSystemAccessData - a model defined in Swagger"""  # noqa: E501
        self._account = None
        self._password = None
        self._username = None
        self._apikey = None
        self.discriminator = None
        if account is not None:
            self.account = account
        if password is not None:
            self.password = password
        if username is not None:
            self.username = username
        if apikey is not None:
            self.apikey = apikey

    @property
    def account(self):
        """Gets the account of this CreateProfileUserNavSystemAccessData.  # noqa: E501


        :return: The account of this CreateProfileUserNavSystemAccessData.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this CreateProfileUserNavSystemAccessData.


        :param account: The account of this CreateProfileUserNavSystemAccessData.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def password(self):
        """Gets the password of this CreateProfileUserNavSystemAccessData.  # noqa: E501


        :return: The password of this CreateProfileUserNavSystemAccessData.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateProfileUserNavSystemAccessData.


        :param password: The password of this CreateProfileUserNavSystemAccessData.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def username(self):
        """Gets the username of this CreateProfileUserNavSystemAccessData.  # noqa: E501


        :return: The username of this CreateProfileUserNavSystemAccessData.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CreateProfileUserNavSystemAccessData.


        :param username: The username of this CreateProfileUserNavSystemAccessData.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def apikey(self):
        """Gets the apikey of this CreateProfileUserNavSystemAccessData.  # noqa: E501


        :return: The apikey of this CreateProfileUserNavSystemAccessData.  # noqa: E501
        :rtype: str
        """
        return self._apikey

    @apikey.setter
    def apikey(self, apikey):
        """Sets the apikey of this CreateProfileUserNavSystemAccessData.


        :param apikey: The apikey of this CreateProfileUserNavSystemAccessData.  # noqa: E501
        :type: str
        """

        self._apikey = apikey

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
        if issubclass(CreateProfileUserNavSystemAccessData, dict):
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
        if not isinstance(other, CreateProfileUserNavSystemAccessData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other