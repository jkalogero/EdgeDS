# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.security_info import SecurityInfo  # noqa: F401,E501
from swagger_server.models.transport_type import TransportType  # noqa: F401,E501
from swagger_server.models.one_of_transport_info_endpoint import OneOfTransportInfoEndpoint  # noqa: F401,E501
from swagger_server import util


class TransportInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, name: str=None, description: str=None, type: TransportType=None, protocol: str=None, version: str=None, endpoint: OneOfTransportInfoEndpoint=None, security: SecurityInfo=None, impl_specific_info: object=None):  # noqa: E501
        """TransportInfo - a model defined in Swagger

        :param id: The id of this TransportInfo.  # noqa: E501
        :type id: str
        :param name: The name of this TransportInfo.  # noqa: E501
        :type name: str
        :param description: The description of this TransportInfo.  # noqa: E501
        :type description: str
        :param type: The type of this TransportInfo.  # noqa: E501
        :type type: TransportType
        :param protocol: The protocol of this TransportInfo.  # noqa: E501
        :type protocol: str
        :param version: The version of this TransportInfo.  # noqa: E501
        :type version: str
        :param endpoint: The endpoint of this TransportInfo.  # noqa: E501
        :type endpoint: OneOfTransportInfoEndpoint
        :param security: The security of this TransportInfo.  # noqa: E501
        :type security: SecurityInfo
        :param impl_specific_info: The impl_specific_info of this TransportInfo.  # noqa: E501
        :type impl_specific_info: object
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'description': str,
            'type': TransportType,
            'protocol': str,
            'version': str,
            'endpoint': OneOfTransportInfoEndpoint,
            'security': SecurityInfo,
            'impl_specific_info': object
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'type': 'type',
            'protocol': 'protocol',
            'version': 'version',
            'endpoint': 'endpoint',
            'security': 'security',
            'impl_specific_info': 'implSpecificInfo'
        }
        self._id = id
        self._name = name
        self._description = description
        self._type = type
        self._protocol = protocol
        self._version = version
        self._endpoint = endpoint
        self._security = security
        self._impl_specific_info = impl_specific_info

    @classmethod
    def from_dict(cls, dikt) -> 'TransportInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TransportInfo of this TransportInfo.  # noqa: E501
        :rtype: TransportInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this TransportInfo.

        The identifier of this transport  # noqa: E501

        :return: The id of this TransportInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this TransportInfo.

        The identifier of this transport  # noqa: E501

        :param id: The id of this TransportInfo.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this TransportInfo.

        The name of this transport  # noqa: E501

        :return: The name of this TransportInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this TransportInfo.

        The name of this transport  # noqa: E501

        :param name: The name of this TransportInfo.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this TransportInfo.

        Human-readable description of this transport  # noqa: E501

        :return: The description of this TransportInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this TransportInfo.

        Human-readable description of this transport  # noqa: E501

        :param description: The description of this TransportInfo.
        :type description: str
        """

        self._description = description

    @property
    def type(self) -> TransportType:
        """Gets the type of this TransportInfo.


        :return: The type of this TransportInfo.
        :rtype: TransportType
        """
        return self._type

    @type.setter
    def type(self, type: TransportType):
        """Sets the type of this TransportInfo.


        :param type: The type of this TransportInfo.
        :type type: TransportType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def protocol(self) -> str:
        """Gets the protocol of this TransportInfo.

        The name of the protocol used. Shall be set to HTTP for a REST API.  # noqa: E501

        :return: The protocol of this TransportInfo.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol: str):
        """Sets the protocol of this TransportInfo.

        The name of the protocol used. Shall be set to HTTP for a REST API.  # noqa: E501

        :param protocol: The protocol of this TransportInfo.
        :type protocol: str
        """
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

    @property
    def version(self) -> str:
        """Gets the version of this TransportInfo.

        The version of the protocol used  # noqa: E501

        :return: The version of this TransportInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this TransportInfo.

        The version of the protocol used  # noqa: E501

        :param version: The version of this TransportInfo.
        :type version: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def endpoint(self) -> OneOfTransportInfoEndpoint:
        """Gets the endpoint of this TransportInfo.

        This type represents information about a transport endpoint  # noqa: E501

        :return: The endpoint of this TransportInfo.
        :rtype: OneOfTransportInfoEndpoint
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint: OneOfTransportInfoEndpoint):
        """Sets the endpoint of this TransportInfo.

        This type represents information about a transport endpoint  # noqa: E501

        :param endpoint: The endpoint of this TransportInfo.
        :type endpoint: OneOfTransportInfoEndpoint
        """
        if endpoint is None:
            raise ValueError("Invalid value for `endpoint`, must not be `None`")  # noqa: E501

        self._endpoint = endpoint

    @property
    def security(self) -> SecurityInfo:
        """Gets the security of this TransportInfo.


        :return: The security of this TransportInfo.
        :rtype: SecurityInfo
        """
        return self._security

    @security.setter
    def security(self, security: SecurityInfo):
        """Sets the security of this TransportInfo.


        :param security: The security of this TransportInfo.
        :type security: SecurityInfo
        """
        if security is None:
            raise ValueError("Invalid value for `security`, must not be `None`")  # noqa: E501

        self._security = security

    @property
    def impl_specific_info(self) -> object:
        """Gets the impl_specific_info of this TransportInfo.

        Additional implementation specific details of the transport  # noqa: E501

        :return: The impl_specific_info of this TransportInfo.
        :rtype: object
        """
        return self._impl_specific_info

    @impl_specific_info.setter
    def impl_specific_info(self, impl_specific_info: object):
        """Sets the impl_specific_info of this TransportInfo.

        Additional implementation specific details of the transport  # noqa: E501

        :param impl_specific_info: The impl_specific_info of this TransportInfo.
        :type impl_specific_info: object
        """

        self._impl_specific_info = impl_specific_info
