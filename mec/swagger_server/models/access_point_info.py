# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.connection_type import ConnectionType  # noqa: F401,E501
from swagger_server.models.location_info import LocationInfo  # noqa: F401,E501
from swagger_server.models.operation_status import OperationStatus  # noqa: F401,E501
from swagger_server import util


class AccessPointInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, access_point_id: str=None, connection_type: ConnectionType=None, interest_realm: str=None, location_info: LocationInfo=None, number_of_users: int=None, operation_status: OperationStatus=None, resource_url: str=None, timezone: str=None):  # noqa: E501
        """AccessPointInfo - a model defined in Swagger

        :param access_point_id: The access_point_id of this AccessPointInfo.  # noqa: E501
        :type access_point_id: str
        :param connection_type: The connection_type of this AccessPointInfo.  # noqa: E501
        :type connection_type: ConnectionType
        :param interest_realm: The interest_realm of this AccessPointInfo.  # noqa: E501
        :type interest_realm: str
        :param location_info: The location_info of this AccessPointInfo.  # noqa: E501
        :type location_info: LocationInfo
        :param number_of_users: The number_of_users of this AccessPointInfo.  # noqa: E501
        :type number_of_users: int
        :param operation_status: The operation_status of this AccessPointInfo.  # noqa: E501
        :type operation_status: OperationStatus
        :param resource_url: The resource_url of this AccessPointInfo.  # noqa: E501
        :type resource_url: str
        :param timezone: The timezone of this AccessPointInfo.  # noqa: E501
        :type timezone: str
        """
        self.swagger_types = {
            'access_point_id': str,
            'connection_type': ConnectionType,
            'interest_realm': str,
            'location_info': LocationInfo,
            'number_of_users': int,
            'operation_status': OperationStatus,
            'resource_url': str,
            'timezone': str
        }

        self.attribute_map = {
            'access_point_id': 'accessPointId',
            'connection_type': 'connectionType',
            'interest_realm': 'interestRealm',
            'location_info': 'locationInfo',
            'number_of_users': 'numberOfUsers',
            'operation_status': 'operationStatus',
            'resource_url': 'resourceURL',
            'timezone': 'timezone'
        }
        self._access_point_id = access_point_id
        self._connection_type = connection_type
        self._interest_realm = interest_realm
        self._location_info = location_info
        self._number_of_users = number_of_users
        self._operation_status = operation_status
        self._resource_url = resource_url
        self._timezone = timezone

    @classmethod
    def from_dict(cls, dikt) -> 'AccessPointInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AccessPointInfo of this AccessPointInfo.  # noqa: E501
        :rtype: AccessPointInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def access_point_id(self) -> str:
        """Gets the access_point_id of this AccessPointInfo.

        Identifier of access point.  # noqa: E501

        :return: The access_point_id of this AccessPointInfo.
        :rtype: str
        """
        return self._access_point_id

    @access_point_id.setter
    def access_point_id(self, access_point_id: str):
        """Sets the access_point_id of this AccessPointInfo.

        Identifier of access point.  # noqa: E501

        :param access_point_id: The access_point_id of this AccessPointInfo.
        :type access_point_id: str
        """
        if access_point_id is None:
            raise ValueError("Invalid value for `access_point_id`, must not be `None`")  # noqa: E501

        self._access_point_id = access_point_id

    @property
    def connection_type(self) -> ConnectionType:
        """Gets the connection_type of this AccessPointInfo.


        :return: The connection_type of this AccessPointInfo.
        :rtype: ConnectionType
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type: ConnectionType):
        """Sets the connection_type of this AccessPointInfo.


        :param connection_type: The connection_type of this AccessPointInfo.
        :type connection_type: ConnectionType
        """
        if connection_type is None:
            raise ValueError("Invalid value for `connection_type`, must not be `None`")  # noqa: E501

        self._connection_type = connection_type

    @property
    def interest_realm(self) -> str:
        """Gets the interest_realm of this AccessPointInfo.

        Interest realm of access point.  # noqa: E501

        :return: The interest_realm of this AccessPointInfo.
        :rtype: str
        """
        return self._interest_realm

    @interest_realm.setter
    def interest_realm(self, interest_realm: str):
        """Sets the interest_realm of this AccessPointInfo.

        Interest realm of access point.  # noqa: E501

        :param interest_realm: The interest_realm of this AccessPointInfo.
        :type interest_realm: str
        """

        self._interest_realm = interest_realm

    @property
    def location_info(self) -> LocationInfo:
        """Gets the location_info of this AccessPointInfo.


        :return: The location_info of this AccessPointInfo.
        :rtype: LocationInfo
        """
        return self._location_info

    @location_info.setter
    def location_info(self, location_info: LocationInfo):
        """Sets the location_info of this AccessPointInfo.


        :param location_info: The location_info of this AccessPointInfo.
        :type location_info: LocationInfo
        """

        self._location_info = location_info

    @property
    def number_of_users(self) -> int:
        """Gets the number_of_users of this AccessPointInfo.

        Number of users currently on the access point.  # noqa: E501

        :return: The number_of_users of this AccessPointInfo.
        :rtype: int
        """
        return self._number_of_users

    @number_of_users.setter
    def number_of_users(self, number_of_users: int):
        """Sets the number_of_users of this AccessPointInfo.

        Number of users currently on the access point.  # noqa: E501

        :param number_of_users: The number_of_users of this AccessPointInfo.
        :type number_of_users: int
        """
        if number_of_users is None:
            raise ValueError("Invalid value for `number_of_users`, must not be `None`")  # noqa: E501

        self._number_of_users = number_of_users

    @property
    def operation_status(self) -> OperationStatus:
        """Gets the operation_status of this AccessPointInfo.


        :return: The operation_status of this AccessPointInfo.
        :rtype: OperationStatus
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status: OperationStatus):
        """Sets the operation_status of this AccessPointInfo.


        :param operation_status: The operation_status of this AccessPointInfo.
        :type operation_status: OperationStatus
        """
        if operation_status is None:
            raise ValueError("Invalid value for `operation_status`, must not be `None`")  # noqa: E501

        self._operation_status = operation_status

    @property
    def resource_url(self) -> str:
        """Gets the resource_url of this AccessPointInfo.

        Self referring URL  # noqa: E501

        :return: The resource_url of this AccessPointInfo.
        :rtype: str
        """
        return self._resource_url

    @resource_url.setter
    def resource_url(self, resource_url: str):
        """Sets the resource_url of this AccessPointInfo.

        Self referring URL  # noqa: E501

        :param resource_url: The resource_url of this AccessPointInfo.
        :type resource_url: str
        """
        if resource_url is None:
            raise ValueError("Invalid value for `resource_url`, must not be `None`")  # noqa: E501

        self._resource_url = resource_url

    @property
    def timezone(self) -> str:
        """Gets the timezone of this AccessPointInfo.

        Time zone of access point.  # noqa: E501

        :return: The timezone of this AccessPointInfo.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone: str):
        """Sets the timezone of this AccessPointInfo.

        Time zone of access point.  # noqa: E501

        :param timezone: The timezone of this AccessPointInfo.
        :type timezone: str
        """

        self._timezone = timezone
