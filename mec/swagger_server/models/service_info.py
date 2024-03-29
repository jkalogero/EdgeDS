# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.category_ref import CategoryRef  # noqa: F401,E501
from swagger_server.models.locality_type import LocalityType  # noqa: F401,E501
from swagger_server.models.serializer_type import SerializerType  # noqa: F401,E501
from swagger_server.models.service_info_links import ServiceInfoLinks  # noqa: F401,E501
from swagger_server.models.service_state import ServiceState  # noqa: F401,E501
from swagger_server.models.transport_info import TransportInfo  # noqa: F401,E501
from swagger_server import util


class ServiceInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ser_instance_id: str=None, ser_name: str=None, ser_category: CategoryRef=None, version: str=None, state: ServiceState=None, transport_info: TransportInfo=None, serializer: SerializerType=None, scope_of_locality: LocalityType=None, consumed_local_only: bool=None, is_local: bool=None, liveness_interval: int=None, links: ServiceInfoLinks=None):  # noqa: E501
        """ServiceInfo - a model defined in Swagger

        :param ser_instance_id: The ser_instance_id of this ServiceInfo.  # noqa: E501
        :type ser_instance_id: str
        :param ser_name: The ser_name of this ServiceInfo.  # noqa: E501
        :type ser_name: str
        :param ser_category: The ser_category of this ServiceInfo.  # noqa: E501
        :type ser_category: CategoryRef
        :param version: The version of this ServiceInfo.  # noqa: E501
        :type version: str
        :param state: The state of this ServiceInfo.  # noqa: E501
        :type state: ServiceState
        :param transport_info: The transport_info of this ServiceInfo.  # noqa: E501
        :type transport_info: TransportInfo
        :param serializer: The serializer of this ServiceInfo.  # noqa: E501
        :type serializer: SerializerType
        :param scope_of_locality: The scope_of_locality of this ServiceInfo.  # noqa: E501
        :type scope_of_locality: LocalityType
        :param consumed_local_only: The consumed_local_only of this ServiceInfo.  # noqa: E501
        :type consumed_local_only: bool
        :param is_local: The is_local of this ServiceInfo.  # noqa: E501
        :type is_local: bool
        :param liveness_interval: The liveness_interval of this ServiceInfo.  # noqa: E501
        :type liveness_interval: int
        :param links: The links of this ServiceInfo.  # noqa: E501
        :type links: ServiceInfoLinks
        """
        self.swagger_types = {
            'ser_instance_id': str,
            'ser_name': str,
            'ser_category': CategoryRef,
            'version': str,
            'state': ServiceState,
            'transport_info': TransportInfo,
            'serializer': SerializerType,
            'scope_of_locality': LocalityType,
            'consumed_local_only': bool,
            'is_local': bool,
            'liveness_interval': int,
            'links': ServiceInfoLinks
        }

        self.attribute_map = {
            'ser_instance_id': 'serInstanceId',
            'ser_name': 'serName',
            'ser_category': 'serCategory',
            'version': 'version',
            'state': 'state',
            'transport_info': 'transportInfo',
            'serializer': 'serializer',
            'scope_of_locality': 'scopeOfLocality',
            'consumed_local_only': 'consumedLocalOnly',
            'is_local': 'isLocal',
            'liveness_interval': 'livenessInterval',
            'links': '_links'
        }
        self._ser_instance_id = ser_instance_id
        self._ser_name = ser_name
        self._ser_category = ser_category
        self._version = version
        self._state = state
        self._transport_info = transport_info
        self._serializer = serializer
        self._scope_of_locality = scope_of_locality
        self._consumed_local_only = consumed_local_only
        self._is_local = is_local
        self._liveness_interval = liveness_interval
        self._links = links

    @classmethod
    def from_dict(cls, dikt) -> 'ServiceInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ServiceInfo of this ServiceInfo.  # noqa: E501
        :rtype: ServiceInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ser_instance_id(self) -> str:
        """Gets the ser_instance_id of this ServiceInfo.

        Identifier of the service instance assigned by the MEC platform.  # noqa: E501

        :return: The ser_instance_id of this ServiceInfo.
        :rtype: str
        """
        return self._ser_instance_id

    @ser_instance_id.setter
    def ser_instance_id(self, ser_instance_id: str):
        """Sets the ser_instance_id of this ServiceInfo.

        Identifier of the service instance assigned by the MEC platform.  # noqa: E501

        :param ser_instance_id: The ser_instance_id of this ServiceInfo.
        :type ser_instance_id: str
        """

        self._ser_instance_id = ser_instance_id

    @property
    def ser_name(self) -> str:
        """Gets the ser_name of this ServiceInfo.

        The name of the service. This is how the service producing MEC application identifies the service instance it produces.  # noqa: E501

        :return: The ser_name of this ServiceInfo.
        :rtype: str
        """
        return self._ser_name

    @ser_name.setter
    def ser_name(self, ser_name: str):
        """Sets the ser_name of this ServiceInfo.

        The name of the service. This is how the service producing MEC application identifies the service instance it produces.  # noqa: E501

        :param ser_name: The ser_name of this ServiceInfo.
        :type ser_name: str
        """
        if ser_name is None:
            raise ValueError("Invalid value for `ser_name`, must not be `None`")  # noqa: E501

        self._ser_name = ser_name

    @property
    def ser_category(self) -> CategoryRef:
        """Gets the ser_category of this ServiceInfo.


        :return: The ser_category of this ServiceInfo.
        :rtype: CategoryRef
        """
        return self._ser_category

    @ser_category.setter
    def ser_category(self, ser_category: CategoryRef):
        """Sets the ser_category of this ServiceInfo.


        :param ser_category: The ser_category of this ServiceInfo.
        :type ser_category: CategoryRef
        """

        self._ser_category = ser_category

    @property
    def version(self) -> str:
        """Gets the version of this ServiceInfo.

        Service version  # noqa: E501

        :return: The version of this ServiceInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this ServiceInfo.

        Service version  # noqa: E501

        :param version: The version of this ServiceInfo.
        :type version: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def state(self) -> ServiceState:
        """Gets the state of this ServiceInfo.


        :return: The state of this ServiceInfo.
        :rtype: ServiceState
        """
        return self._state

    @state.setter
    def state(self, state: ServiceState):
        """Sets the state of this ServiceInfo.


        :param state: The state of this ServiceInfo.
        :type state: ServiceState
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def transport_info(self) -> TransportInfo:
        """Gets the transport_info of this ServiceInfo.


        :return: The transport_info of this ServiceInfo.
        :rtype: TransportInfo
        """
        return self._transport_info

    @transport_info.setter
    def transport_info(self, transport_info: TransportInfo):
        """Sets the transport_info of this ServiceInfo.


        :param transport_info: The transport_info of this ServiceInfo.
        :type transport_info: TransportInfo
        """
        if transport_info is None:
            raise ValueError("Invalid value for `transport_info`, must not be `None`")  # noqa: E501

        self._transport_info = transport_info

    @property
    def serializer(self) -> SerializerType:
        """Gets the serializer of this ServiceInfo.


        :return: The serializer of this ServiceInfo.
        :rtype: SerializerType
        """
        return self._serializer

    @serializer.setter
    def serializer(self, serializer: SerializerType):
        """Sets the serializer of this ServiceInfo.


        :param serializer: The serializer of this ServiceInfo.
        :type serializer: SerializerType
        """
        if serializer is None:
            raise ValueError("Invalid value for `serializer`, must not be `None`")  # noqa: E501

        self._serializer = serializer

    @property
    def scope_of_locality(self) -> LocalityType:
        """Gets the scope_of_locality of this ServiceInfo.


        :return: The scope_of_locality of this ServiceInfo.
        :rtype: LocalityType
        """
        return self._scope_of_locality

    @scope_of_locality.setter
    def scope_of_locality(self, scope_of_locality: LocalityType):
        """Sets the scope_of_locality of this ServiceInfo.


        :param scope_of_locality: The scope_of_locality of this ServiceInfo.
        :type scope_of_locality: LocalityType
        """

        self._scope_of_locality = scope_of_locality

    @property
    def consumed_local_only(self) -> bool:
        """Gets the consumed_local_only of this ServiceInfo.

        Indicate whether the service can only be consumed by the MEC applications located in the same locality (as defined by scopeOfLocality) as this  service instance.  # noqa: E501

        :return: The consumed_local_only of this ServiceInfo.
        :rtype: bool
        """
        return self._consumed_local_only

    @consumed_local_only.setter
    def consumed_local_only(self, consumed_local_only: bool):
        """Sets the consumed_local_only of this ServiceInfo.

        Indicate whether the service can only be consumed by the MEC applications located in the same locality (as defined by scopeOfLocality) as this  service instance.  # noqa: E501

        :param consumed_local_only: The consumed_local_only of this ServiceInfo.
        :type consumed_local_only: bool
        """

        self._consumed_local_only = consumed_local_only

    @property
    def is_local(self) -> bool:
        """Gets the is_local of this ServiceInfo.

        Indicate whether the service is located in the same locality (as defined by scopeOfLocality) as the consuming MEC application.  # noqa: E501

        :return: The is_local of this ServiceInfo.
        :rtype: bool
        """
        return self._is_local

    @is_local.setter
    def is_local(self, is_local: bool):
        """Sets the is_local of this ServiceInfo.

        Indicate whether the service is located in the same locality (as defined by scopeOfLocality) as the consuming MEC application.  # noqa: E501

        :param is_local: The is_local of this ServiceInfo.
        :type is_local: bool
        """

        self._is_local = is_local

    @property
    def liveness_interval(self) -> int:
        """Gets the liveness_interval of this ServiceInfo.

        Interval (in seconds) between two consecutive \"heartbeat\" messages (see clause 8.2.10.3.3). If the service-producing application supports sending \"heartbeat\" messages, it shall include this attribute in the swagger_server request. In this case, the application shall either set the value of this attribute to zero or shall use this attribute to propose a non-zero positive value for the liveness interval. If the application has provided this attribute in the request and the MEC platform requires \"heartbeat\" messages, the MEC platform shall return this attribute value in the HTTP responses. The MEC platform may use the value proposed in the request or may choose a different value. If the MEC platform does not require \"heartbeat\" messages for this service instance it shall omit the attribute in responses.  # noqa: E501

        :return: The liveness_interval of this ServiceInfo.
        :rtype: int
        """
        return self._liveness_interval

    @liveness_interval.setter
    def liveness_interval(self, liveness_interval: int):
        """Sets the liveness_interval of this ServiceInfo.

        Interval (in seconds) between two consecutive \"heartbeat\" messages (see clause 8.2.10.3.3). If the service-producing application supports sending \"heartbeat\" messages, it shall include this attribute in the swagger_server request. In this case, the application shall either set the value of this attribute to zero or shall use this attribute to propose a non-zero positive value for the liveness interval. If the application has provided this attribute in the request and the MEC platform requires \"heartbeat\" messages, the MEC platform shall return this attribute value in the HTTP responses. The MEC platform may use the value proposed in the request or may choose a different value. If the MEC platform does not require \"heartbeat\" messages for this service instance it shall omit the attribute in responses.  # noqa: E501

        :param liveness_interval: The liveness_interval of this ServiceInfo.
        :type liveness_interval: int
        """

        self._liveness_interval = liveness_interval

    @property
    def links(self) -> ServiceInfoLinks:
        """Gets the links of this ServiceInfo.


        :return: The links of this ServiceInfo.
        :rtype: ServiceInfoLinks
        """
        return self._links

    @links.setter
    def links(self, links: ServiceInfoLinks):
        """Sets the links of this ServiceInfo.


        :param links: The links of this ServiceInfo.
        :type links: ServiceInfoLinks
        """

        self._links = links
