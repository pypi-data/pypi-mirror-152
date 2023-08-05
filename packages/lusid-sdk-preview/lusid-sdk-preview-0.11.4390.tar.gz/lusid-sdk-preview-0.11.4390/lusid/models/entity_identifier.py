# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4390
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class EntityIdentifier(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'identifier_scope': 'str',
        'identifier_type': 'str',
        'identifier_value': 'str'
    }

    attribute_map = {
        'identifier_scope': 'identifierScope',
        'identifier_type': 'identifierType',
        'identifier_value': 'identifierValue'
    }

    required_map = {
        'identifier_scope': 'optional',
        'identifier_type': 'required',
        'identifier_value': 'required'
    }

    def __init__(self, identifier_scope=None, identifier_type=None, identifier_value=None, local_vars_configuration=None):  # noqa: E501
        """EntityIdentifier - a model defined in OpenAPI"
        
        :param identifier_scope:  The scope of the identifier
        :type identifier_scope: str
        :param identifier_type:  The type of the identifier (required)
        :type identifier_type: str
        :param identifier_value:  The value of the identifier (required)
        :type identifier_value: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._identifier_scope = None
        self._identifier_type = None
        self._identifier_value = None
        self.discriminator = None

        self.identifier_scope = identifier_scope
        self.identifier_type = identifier_type
        self.identifier_value = identifier_value

    @property
    def identifier_scope(self):
        """Gets the identifier_scope of this EntityIdentifier.  # noqa: E501

        The scope of the identifier  # noqa: E501

        :return: The identifier_scope of this EntityIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._identifier_scope

    @identifier_scope.setter
    def identifier_scope(self, identifier_scope):
        """Sets the identifier_scope of this EntityIdentifier.

        The scope of the identifier  # noqa: E501

        :param identifier_scope: The identifier_scope of this EntityIdentifier.  # noqa: E501
        :type identifier_scope: str
        """

        self._identifier_scope = identifier_scope

    @property
    def identifier_type(self):
        """Gets the identifier_type of this EntityIdentifier.  # noqa: E501

        The type of the identifier  # noqa: E501

        :return: The identifier_type of this EntityIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._identifier_type

    @identifier_type.setter
    def identifier_type(self, identifier_type):
        """Sets the identifier_type of this EntityIdentifier.

        The type of the identifier  # noqa: E501

        :param identifier_type: The identifier_type of this EntityIdentifier.  # noqa: E501
        :type identifier_type: str
        """
        if self.local_vars_configuration.client_side_validation and identifier_type is None:  # noqa: E501
            raise ValueError("Invalid value for `identifier_type`, must not be `None`")  # noqa: E501

        self._identifier_type = identifier_type

    @property
    def identifier_value(self):
        """Gets the identifier_value of this EntityIdentifier.  # noqa: E501

        The value of the identifier  # noqa: E501

        :return: The identifier_value of this EntityIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._identifier_value

    @identifier_value.setter
    def identifier_value(self, identifier_value):
        """Sets the identifier_value of this EntityIdentifier.

        The value of the identifier  # noqa: E501

        :param identifier_value: The identifier_value of this EntityIdentifier.  # noqa: E501
        :type identifier_value: str
        """
        if self.local_vars_configuration.client_side_validation and identifier_value is None:  # noqa: E501
            raise ValueError("Invalid value for `identifier_value`, must not be `None`")  # noqa: E501

        self._identifier_value = identifier_value

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EntityIdentifier):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntityIdentifier):
            return True

        return self.to_dict() != other.to_dict()
