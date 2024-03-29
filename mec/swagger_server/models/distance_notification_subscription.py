# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.callback_reference import CallbackReference  # noqa: F401,E501
from swagger_server.models.distance_criteria import DistanceCriteria  # noqa: F401,E501
from swagger_server.models.link import Link  # noqa: F401,E501
from swagger_server import util


class DistanceNotificationSubscription(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, callback_reference: CallbackReference=None, check_immediate: bool=None, client_correlator: str=None, count: int=None, criteria: DistanceCriteria=None, distance: float=None, duration: int=None, frequency: int=None, link: List[Link]=None, monitored_address: List[str]=None, reference_address: List[str]=None, requester: str=None, resource_url: str=None, tracking_accuracy: float=None):  # noqa: E501
        """DistanceNotificationSubscription - a model defined in Swagger

        :param callback_reference: The callback_reference of this DistanceNotificationSubscription.  # noqa: E501
        :type callback_reference: CallbackReference
        :param check_immediate: The check_immediate of this DistanceNotificationSubscription.  # noqa: E501
        :type check_immediate: bool
        :param client_correlator: The client_correlator of this DistanceNotificationSubscription.  # noqa: E501
        :type client_correlator: str
        :param count: The count of this DistanceNotificationSubscription.  # noqa: E501
        :type count: int
        :param criteria: The criteria of this DistanceNotificationSubscription.  # noqa: E501
        :type criteria: DistanceCriteria
        :param distance: The distance of this DistanceNotificationSubscription.  # noqa: E501
        :type distance: float
        :param duration: The duration of this DistanceNotificationSubscription.  # noqa: E501
        :type duration: int
        :param frequency: The frequency of this DistanceNotificationSubscription.  # noqa: E501
        :type frequency: int
        :param link: The link of this DistanceNotificationSubscription.  # noqa: E501
        :type link: List[Link]
        :param monitored_address: The monitored_address of this DistanceNotificationSubscription.  # noqa: E501
        :type monitored_address: List[str]
        :param reference_address: The reference_address of this DistanceNotificationSubscription.  # noqa: E501
        :type reference_address: List[str]
        :param requester: The requester of this DistanceNotificationSubscription.  # noqa: E501
        :type requester: str
        :param resource_url: The resource_url of this DistanceNotificationSubscription.  # noqa: E501
        :type resource_url: str
        :param tracking_accuracy: The tracking_accuracy of this DistanceNotificationSubscription.  # noqa: E501
        :type tracking_accuracy: float
        """
        self.swagger_types = {
            'callback_reference': CallbackReference,
            'check_immediate': bool,
            'client_correlator': str,
            'count': int,
            'criteria': DistanceCriteria,
            'distance': float,
            'duration': int,
            'frequency': int,
            'link': List[Link],
            'monitored_address': List[str],
            'reference_address': List[str],
            'requester': str,
            'resource_url': str,
            'tracking_accuracy': float
        }

        self.attribute_map = {
            'callback_reference': 'callbackReference',
            'check_immediate': 'checkImmediate',
            'client_correlator': 'clientCorrelator',
            'count': 'count',
            'criteria': 'criteria',
            'distance': 'distance',
            'duration': 'duration',
            'frequency': 'frequency',
            'link': 'link',
            'monitored_address': 'monitoredAddress',
            'reference_address': 'referenceAddress',
            'requester': 'requester',
            'resource_url': 'resourceURL',
            'tracking_accuracy': 'trackingAccuracy'
        }
        self._callback_reference = callback_reference
        self._check_immediate = check_immediate
        self._client_correlator = client_correlator
        self._count = count
        self._criteria = criteria
        self._distance = distance
        self._duration = duration
        self._frequency = frequency
        self._link = link
        self._monitored_address = monitored_address
        self._reference_address = reference_address
        self._requester = requester
        self._resource_url = resource_url
        self._tracking_accuracy = tracking_accuracy

    @classmethod
    def from_dict(cls, dikt) -> 'DistanceNotificationSubscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DistanceNotificationSubscription of this DistanceNotificationSubscription.  # noqa: E501
        :rtype: DistanceNotificationSubscription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def callback_reference(self) -> CallbackReference:
        """Gets the callback_reference of this DistanceNotificationSubscription.


        :return: The callback_reference of this DistanceNotificationSubscription.
        :rtype: CallbackReference
        """
        return self._callback_reference

    @callback_reference.setter
    def callback_reference(self, callback_reference: CallbackReference):
        """Sets the callback_reference of this DistanceNotificationSubscription.


        :param callback_reference: The callback_reference of this DistanceNotificationSubscription.
        :type callback_reference: CallbackReference
        """
        if callback_reference is None:
            raise ValueError("Invalid value for `callback_reference`, must not be `None`")  # noqa: E501

        self._callback_reference = callback_reference

    @property
    def check_immediate(self) -> bool:
        """Gets the check_immediate of this DistanceNotificationSubscription.

        Check location immediately after establishing notification.  # noqa: E501

        :return: The check_immediate of this DistanceNotificationSubscription.
        :rtype: bool
        """
        return self._check_immediate

    @check_immediate.setter
    def check_immediate(self, check_immediate: bool):
        """Sets the check_immediate of this DistanceNotificationSubscription.

        Check location immediately after establishing notification.  # noqa: E501

        :param check_immediate: The check_immediate of this DistanceNotificationSubscription.
        :type check_immediate: bool
        """
        if check_immediate is None:
            raise ValueError("Invalid value for `check_immediate`, must not be `None`")  # noqa: E501

        self._check_immediate = check_immediate

    @property
    def client_correlator(self) -> str:
        """Gets the client_correlator of this DistanceNotificationSubscription.

        A correlator that the client can use to tag this particular resource representation during a request to create a resource on the server.  # noqa: E501

        :return: The client_correlator of this DistanceNotificationSubscription.
        :rtype: str
        """
        return self._client_correlator

    @client_correlator.setter
    def client_correlator(self, client_correlator: str):
        """Sets the client_correlator of this DistanceNotificationSubscription.

        A correlator that the client can use to tag this particular resource representation during a request to create a resource on the server.  # noqa: E501

        :param client_correlator: The client_correlator of this DistanceNotificationSubscription.
        :type client_correlator: str
        """

        self._client_correlator = client_correlator

    @property
    def count(self) -> int:
        """Gets the count of this DistanceNotificationSubscription.

        Maximum number of notifications per individual address. For no maximum, either do not include this element or specify a value of zero. Default value is 0.  # noqa: E501

        :return: The count of this DistanceNotificationSubscription.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int):
        """Sets the count of this DistanceNotificationSubscription.

        Maximum number of notifications per individual address. For no maximum, either do not include this element or specify a value of zero. Default value is 0.  # noqa: E501

        :param count: The count of this DistanceNotificationSubscription.
        :type count: int
        """

        self._count = count

    @property
    def criteria(self) -> DistanceCriteria:
        """Gets the criteria of this DistanceNotificationSubscription.


        :return: The criteria of this DistanceNotificationSubscription.
        :rtype: DistanceCriteria
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria: DistanceCriteria):
        """Sets the criteria of this DistanceNotificationSubscription.


        :param criteria: The criteria of this DistanceNotificationSubscription.
        :type criteria: DistanceCriteria
        """
        if criteria is None:
            raise ValueError("Invalid value for `criteria`, must not be `None`")  # noqa: E501

        self._criteria = criteria

    @property
    def distance(self) -> float:
        """Gets the distance of this DistanceNotificationSubscription.

        Distance between devices that shall be monitored.  # noqa: E501

        :return: The distance of this DistanceNotificationSubscription.
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance: float):
        """Sets the distance of this DistanceNotificationSubscription.

        Distance between devices that shall be monitored.  # noqa: E501

        :param distance: The distance of this DistanceNotificationSubscription.
        :type distance: float
        """
        if distance is None:
            raise ValueError("Invalid value for `distance`, must not be `None`")  # noqa: E501

        self._distance = distance

    @property
    def duration(self) -> int:
        """Gets the duration of this DistanceNotificationSubscription.

        Period of time (in seconds) notifications are provided for. If set to “0” (zero), a default duration time, which is specified by the service policy, will be used. If the parameter is omitted, the notifications will continue until the maximum duration time, which is specified by the service policy, unless the notifications are stopped by deletion of subscription for notifications.  # noqa: E501

        :return: The duration of this DistanceNotificationSubscription.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration: int):
        """Sets the duration of this DistanceNotificationSubscription.

        Period of time (in seconds) notifications are provided for. If set to “0” (zero), a default duration time, which is specified by the service policy, will be used. If the parameter is omitted, the notifications will continue until the maximum duration time, which is specified by the service policy, unless the notifications are stopped by deletion of subscription for notifications.  # noqa: E501

        :param duration: The duration of this DistanceNotificationSubscription.
        :type duration: int
        """

        self._duration = duration

    @property
    def frequency(self) -> int:
        """Gets the frequency of this DistanceNotificationSubscription.

        Maximum frequency (in seconds) of notifications per subscription (can also be considered minimum time between notifications).  # noqa: E501

        :return: The frequency of this DistanceNotificationSubscription.
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency: int):
        """Sets the frequency of this DistanceNotificationSubscription.

        Maximum frequency (in seconds) of notifications per subscription (can also be considered minimum time between notifications).  # noqa: E501

        :param frequency: The frequency of this DistanceNotificationSubscription.
        :type frequency: int
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")  # noqa: E501

        self._frequency = frequency

    @property
    def link(self) -> List[Link]:
        """Gets the link of this DistanceNotificationSubscription.

        Link to other resources that are in relationship with the resource.  # noqa: E501

        :return: The link of this DistanceNotificationSubscription.
        :rtype: List[Link]
        """
        return self._link

    @link.setter
    def link(self, link: List[Link]):
        """Sets the link of this DistanceNotificationSubscription.

        Link to other resources that are in relationship with the resource.  # noqa: E501

        :param link: The link of this DistanceNotificationSubscription.
        :type link: List[Link]
        """

        self._link = link

    @property
    def monitored_address(self) -> List[str]:
        """Gets the monitored_address of this DistanceNotificationSubscription.

        Contains addresses of devices to monitor (e.g., 'sip' URI, 'tel' URI, 'acr' URI)  # noqa: E501

        :return: The monitored_address of this DistanceNotificationSubscription.
        :rtype: List[str]
        """
        return self._monitored_address

    @monitored_address.setter
    def monitored_address(self, monitored_address: List[str]):
        """Sets the monitored_address of this DistanceNotificationSubscription.

        Contains addresses of devices to monitor (e.g., 'sip' URI, 'tel' URI, 'acr' URI)  # noqa: E501

        :param monitored_address: The monitored_address of this DistanceNotificationSubscription.
        :type monitored_address: List[str]
        """
        if monitored_address is None:
            raise ValueError("Invalid value for `monitored_address`, must not be `None`")  # noqa: E501

        self._monitored_address = monitored_address

    @property
    def reference_address(self) -> List[str]:
        """Gets the reference_address of this DistanceNotificationSubscription.

        Indicates address of each device that will be used as reference devices from which the distances towards monitored devices indicated in the Addresses will be monitored (e.g., 'sip' URI, 'tel' URI, 'acr' URI)  # noqa: E501

        :return: The reference_address of this DistanceNotificationSubscription.
        :rtype: List[str]
        """
        return self._reference_address

    @reference_address.setter
    def reference_address(self, reference_address: List[str]):
        """Sets the reference_address of this DistanceNotificationSubscription.

        Indicates address of each device that will be used as reference devices from which the distances towards monitored devices indicated in the Addresses will be monitored (e.g., 'sip' URI, 'tel' URI, 'acr' URI)  # noqa: E501

        :param reference_address: The reference_address of this DistanceNotificationSubscription.
        :type reference_address: List[str]
        """

        self._reference_address = reference_address

    @property
    def requester(self) -> str:
        """Gets the requester of this DistanceNotificationSubscription.

        Identifies the entity that is requesting the information (e.g. \"sip\" URI, \"tel\" URI, \"acr\" URI)  # noqa: E501

        :return: The requester of this DistanceNotificationSubscription.
        :rtype: str
        """
        return self._requester

    @requester.setter
    def requester(self, requester: str):
        """Sets the requester of this DistanceNotificationSubscription.

        Identifies the entity that is requesting the information (e.g. \"sip\" URI, \"tel\" URI, \"acr\" URI)  # noqa: E501

        :param requester: The requester of this DistanceNotificationSubscription.
        :type requester: str
        """

        self._requester = requester

    @property
    def resource_url(self) -> str:
        """Gets the resource_url of this DistanceNotificationSubscription.

        Self referring URL  # noqa: E501

        :return: The resource_url of this DistanceNotificationSubscription.
        :rtype: str
        """
        return self._resource_url

    @resource_url.setter
    def resource_url(self, resource_url: str):
        """Sets the resource_url of this DistanceNotificationSubscription.

        Self referring URL  # noqa: E501

        :param resource_url: The resource_url of this DistanceNotificationSubscription.
        :type resource_url: str
        """

        self._resource_url = resource_url

    @property
    def tracking_accuracy(self) -> float:
        """Gets the tracking_accuracy of this DistanceNotificationSubscription.

        Number of meters of acceptable error in tracking distance.  # noqa: E501

        :return: The tracking_accuracy of this DistanceNotificationSubscription.
        :rtype: float
        """
        return self._tracking_accuracy

    @tracking_accuracy.setter
    def tracking_accuracy(self, tracking_accuracy: float):
        """Sets the tracking_accuracy of this DistanceNotificationSubscription.

        Number of meters of acceptable error in tracking distance.  # noqa: E501

        :param tracking_accuracy: The tracking_accuracy of this DistanceNotificationSubscription.
        :type tracking_accuracy: float
        """
        if tracking_accuracy is None:
            raise ValueError("Invalid value for `tracking_accuracy`, must not be `None`")  # noqa: E501

        self._tracking_accuracy = tracking_accuracy
