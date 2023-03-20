# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.callback_reference import CallbackReference  # noqa: F401,E501
from swagger_server.models.entering_leaving_criteria import EnteringLeavingCriteria  # noqa: F401,E501
from swagger_server.models.link import Link  # noqa: F401,E501
from swagger_server import util


class CircleNotificationSubscription(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, address: List[str]=None, callback_reference: CallbackReference=None, check_immediate: bool=None, client_correlator: str=None, count: int=None, duration: int=None, entering_leaving_criteria: EnteringLeavingCriteria=None, frequency: int=None, latitude: float=None, link: List[Link]=None, longitude: float=None, radius: float=None, requester: str=None, resource_url: str=None, tracking_accuracy: float=None):  # noqa: E501
        """CircleNotificationSubscription - a model defined in Swagger

        :param address: The address of this CircleNotificationSubscription.  # noqa: E501
        :type address: List[str]
        :param callback_reference: The callback_reference of this CircleNotificationSubscription.  # noqa: E501
        :type callback_reference: CallbackReference
        :param check_immediate: The check_immediate of this CircleNotificationSubscription.  # noqa: E501
        :type check_immediate: bool
        :param client_correlator: The client_correlator of this CircleNotificationSubscription.  # noqa: E501
        :type client_correlator: str
        :param count: The count of this CircleNotificationSubscription.  # noqa: E501
        :type count: int
        :param duration: The duration of this CircleNotificationSubscription.  # noqa: E501
        :type duration: int
        :param entering_leaving_criteria: The entering_leaving_criteria of this CircleNotificationSubscription.  # noqa: E501
        :type entering_leaving_criteria: EnteringLeavingCriteria
        :param frequency: The frequency of this CircleNotificationSubscription.  # noqa: E501
        :type frequency: int
        :param latitude: The latitude of this CircleNotificationSubscription.  # noqa: E501
        :type latitude: float
        :param link: The link of this CircleNotificationSubscription.  # noqa: E501
        :type link: List[Link]
        :param longitude: The longitude of this CircleNotificationSubscription.  # noqa: E501
        :type longitude: float
        :param radius: The radius of this CircleNotificationSubscription.  # noqa: E501
        :type radius: float
        :param requester: The requester of this CircleNotificationSubscription.  # noqa: E501
        :type requester: str
        :param resource_url: The resource_url of this CircleNotificationSubscription.  # noqa: E501
        :type resource_url: str
        :param tracking_accuracy: The tracking_accuracy of this CircleNotificationSubscription.  # noqa: E501
        :type tracking_accuracy: float
        """
        self.swagger_types = {
            'address': List[str],
            'callback_reference': CallbackReference,
            'check_immediate': bool,
            'client_correlator': str,
            'count': int,
            'duration': int,
            'entering_leaving_criteria': EnteringLeavingCriteria,
            'frequency': int,
            'latitude': float,
            'link': List[Link],
            'longitude': float,
            'radius': float,
            'requester': str,
            'resource_url': str,
            'tracking_accuracy': float
        }

        self.attribute_map = {
            'address': 'address',
            'callback_reference': 'callbackReference',
            'check_immediate': 'checkImmediate',
            'client_correlator': 'clientCorrelator',
            'count': 'count',
            'duration': 'duration',
            'entering_leaving_criteria': 'enteringLeavingCriteria',
            'frequency': 'frequency',
            'latitude': 'latitude',
            'link': 'link',
            'longitude': 'longitude',
            'radius': 'radius',
            'requester': 'requester',
            'resource_url': 'resourceURL',
            'tracking_accuracy': 'trackingAccuracy'
        }
        self._address = address
        self._callback_reference = callback_reference
        self._check_immediate = check_immediate
        self._client_correlator = client_correlator
        self._count = count
        self._duration = duration
        self._entering_leaving_criteria = entering_leaving_criteria
        self._frequency = frequency
        self._latitude = latitude
        self._link = link
        self._longitude = longitude
        self._radius = radius
        self._requester = requester
        self._resource_url = resource_url
        self._tracking_accuracy = tracking_accuracy

    @classmethod
    def from_dict(cls, dikt) -> 'CircleNotificationSubscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CircleNotificationSubscription of this CircleNotificationSubscription.  # noqa: E501
        :rtype: CircleNotificationSubscription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self) -> List[str]:
        """Gets the address of this CircleNotificationSubscription.

        Address of terminals to monitor (e.g. \"sip\" URI, \"tel\" URI, \"acr\" URI)  # noqa: E501

        :return: The address of this CircleNotificationSubscription.
        :rtype: List[str]
        """
        return self._address

    @address.setter
    def address(self, address: List[str]):
        """Sets the address of this CircleNotificationSubscription.

        Address of terminals to monitor (e.g. \"sip\" URI, \"tel\" URI, \"acr\" URI)  # noqa: E501

        :param address: The address of this CircleNotificationSubscription.
        :type address: List[str]
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def callback_reference(self) -> CallbackReference:
        """Gets the callback_reference of this CircleNotificationSubscription.


        :return: The callback_reference of this CircleNotificationSubscription.
        :rtype: CallbackReference
        """
        return self._callback_reference

    @callback_reference.setter
    def callback_reference(self, callback_reference: CallbackReference):
        """Sets the callback_reference of this CircleNotificationSubscription.


        :param callback_reference: The callback_reference of this CircleNotificationSubscription.
        :type callback_reference: CallbackReference
        """
        if callback_reference is None:
            raise ValueError("Invalid value for `callback_reference`, must not be `None`")  # noqa: E501

        self._callback_reference = callback_reference

    @property
    def check_immediate(self) -> bool:
        """Gets the check_immediate of this CircleNotificationSubscription.

        Check location immediately after establishing notification.  # noqa: E501

        :return: The check_immediate of this CircleNotificationSubscription.
        :rtype: bool
        """
        return self._check_immediate

    @check_immediate.setter
    def check_immediate(self, check_immediate: bool):
        """Sets the check_immediate of this CircleNotificationSubscription.

        Check location immediately after establishing notification.  # noqa: E501

        :param check_immediate: The check_immediate of this CircleNotificationSubscription.
        :type check_immediate: bool
        """
        if check_immediate is None:
            raise ValueError("Invalid value for `check_immediate`, must not be `None`")  # noqa: E501

        self._check_immediate = check_immediate

    @property
    def client_correlator(self) -> str:
        """Gets the client_correlator of this CircleNotificationSubscription.

        A correlator that the client can use to tag this particular resource representation during a request to create a resource on the server.  # noqa: E501

        :return: The client_correlator of this CircleNotificationSubscription.
        :rtype: str
        """
        return self._client_correlator

    @client_correlator.setter
    def client_correlator(self, client_correlator: str):
        """Sets the client_correlator of this CircleNotificationSubscription.

        A correlator that the client can use to tag this particular resource representation during a request to create a resource on the server.  # noqa: E501

        :param client_correlator: The client_correlator of this CircleNotificationSubscription.
        :type client_correlator: str
        """

        self._client_correlator = client_correlator

    @property
    def count(self) -> int:
        """Gets the count of this CircleNotificationSubscription.

        Maximum number of notifications per individual address. For no maximum, either do not include this element or specify a value of zero. Default value is 0.  # noqa: E501

        :return: The count of this CircleNotificationSubscription.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int):
        """Sets the count of this CircleNotificationSubscription.

        Maximum number of notifications per individual address. For no maximum, either do not include this element or specify a value of zero. Default value is 0.  # noqa: E501

        :param count: The count of this CircleNotificationSubscription.
        :type count: int
        """

        self._count = count

    @property
    def duration(self) -> int:
        """Gets the duration of this CircleNotificationSubscription.

        Period of time (in seconds) notifications are provided for. If set to “0” (zero), a default duration time, which is specified by the service policy, will be used. If the parameter is omitted, the notifications will continue until the maximum duration time, which is specified by the service policy, unless the notifications are stopped by deletion of subscription for notifications.  # noqa: E501

        :return: The duration of this CircleNotificationSubscription.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration: int):
        """Sets the duration of this CircleNotificationSubscription.

        Period of time (in seconds) notifications are provided for. If set to “0” (zero), a default duration time, which is specified by the service policy, will be used. If the parameter is omitted, the notifications will continue until the maximum duration time, which is specified by the service policy, unless the notifications are stopped by deletion of subscription for notifications.  # noqa: E501

        :param duration: The duration of this CircleNotificationSubscription.
        :type duration: int
        """

        self._duration = duration

    @property
    def entering_leaving_criteria(self) -> EnteringLeavingCriteria:
        """Gets the entering_leaving_criteria of this CircleNotificationSubscription.


        :return: The entering_leaving_criteria of this CircleNotificationSubscription.
        :rtype: EnteringLeavingCriteria
        """
        return self._entering_leaving_criteria

    @entering_leaving_criteria.setter
    def entering_leaving_criteria(self, entering_leaving_criteria: EnteringLeavingCriteria):
        """Sets the entering_leaving_criteria of this CircleNotificationSubscription.


        :param entering_leaving_criteria: The entering_leaving_criteria of this CircleNotificationSubscription.
        :type entering_leaving_criteria: EnteringLeavingCriteria
        """
        if entering_leaving_criteria is None:
            raise ValueError("Invalid value for `entering_leaving_criteria`, must not be `None`")  # noqa: E501

        self._entering_leaving_criteria = entering_leaving_criteria

    @property
    def frequency(self) -> int:
        """Gets the frequency of this CircleNotificationSubscription.

        Maximum frequency (in seconds) of notifications per subscription (can also be considered minimum time between notifications).  # noqa: E501

        :return: The frequency of this CircleNotificationSubscription.
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency: int):
        """Sets the frequency of this CircleNotificationSubscription.

        Maximum frequency (in seconds) of notifications per subscription (can also be considered minimum time between notifications).  # noqa: E501

        :param frequency: The frequency of this CircleNotificationSubscription.
        :type frequency: int
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")  # noqa: E501

        self._frequency = frequency

    @property
    def latitude(self) -> float:
        """Gets the latitude of this CircleNotificationSubscription.

        Latitude of center point.  # noqa: E501

        :return: The latitude of this CircleNotificationSubscription.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float):
        """Sets the latitude of this CircleNotificationSubscription.

        Latitude of center point.  # noqa: E501

        :param latitude: The latitude of this CircleNotificationSubscription.
        :type latitude: float
        """
        if latitude is None:
            raise ValueError("Invalid value for `latitude`, must not be `None`")  # noqa: E501

        self._latitude = latitude

    @property
    def link(self) -> List[Link]:
        """Gets the link of this CircleNotificationSubscription.

        Link to other resources that are in relationship with the resource.  # noqa: E501

        :return: The link of this CircleNotificationSubscription.
        :rtype: List[Link]
        """
        return self._link

    @link.setter
    def link(self, link: List[Link]):
        """Sets the link of this CircleNotificationSubscription.

        Link to other resources that are in relationship with the resource.  # noqa: E501

        :param link: The link of this CircleNotificationSubscription.
        :type link: List[Link]
        """

        self._link = link

    @property
    def longitude(self) -> float:
        """Gets the longitude of this CircleNotificationSubscription.

        Longitude of center point.  # noqa: E501

        :return: The longitude of this CircleNotificationSubscription.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float):
        """Sets the longitude of this CircleNotificationSubscription.

        Longitude of center point.  # noqa: E501

        :param longitude: The longitude of this CircleNotificationSubscription.
        :type longitude: float
        """
        if longitude is None:
            raise ValueError("Invalid value for `longitude`, must not be `None`")  # noqa: E501

        self._longitude = longitude

    @property
    def radius(self) -> float:
        """Gets the radius of this CircleNotificationSubscription.

        Radius circle around center point in meters.  # noqa: E501

        :return: The radius of this CircleNotificationSubscription.
        :rtype: float
        """
        return self._radius

    @radius.setter
    def radius(self, radius: float):
        """Sets the radius of this CircleNotificationSubscription.

        Radius circle around center point in meters.  # noqa: E501

        :param radius: The radius of this CircleNotificationSubscription.
        :type radius: float
        """
        if radius is None:
            raise ValueError("Invalid value for `radius`, must not be `None`")  # noqa: E501

        self._radius = radius

    @property
    def requester(self) -> str:
        """Gets the requester of this CircleNotificationSubscription.

        Identifies the entity that is requesting the information (e.g. \"sip\" URI, \"tel\" URI, \"acr\" URI)  # noqa: E501

        :return: The requester of this CircleNotificationSubscription.
        :rtype: str
        """
        return self._requester

    @requester.setter
    def requester(self, requester: str):
        """Sets the requester of this CircleNotificationSubscription.

        Identifies the entity that is requesting the information (e.g. \"sip\" URI, \"tel\" URI, \"acr\" URI)  # noqa: E501

        :param requester: The requester of this CircleNotificationSubscription.
        :type requester: str
        """

        self._requester = requester

    @property
    def resource_url(self) -> str:
        """Gets the resource_url of this CircleNotificationSubscription.

        Self referring URL  # noqa: E501

        :return: The resource_url of this CircleNotificationSubscription.
        :rtype: str
        """
        return self._resource_url

    @resource_url.setter
    def resource_url(self, resource_url: str):
        """Sets the resource_url of this CircleNotificationSubscription.

        Self referring URL  # noqa: E501

        :param resource_url: The resource_url of this CircleNotificationSubscription.
        :type resource_url: str
        """

        self._resource_url = resource_url

    @property
    def tracking_accuracy(self) -> float:
        """Gets the tracking_accuracy of this CircleNotificationSubscription.

        Number of meters of acceptable error in tracking distance.  # noqa: E501

        :return: The tracking_accuracy of this CircleNotificationSubscription.
        :rtype: float
        """
        return self._tracking_accuracy

    @tracking_accuracy.setter
    def tracking_accuracy(self, tracking_accuracy: float):
        """Sets the tracking_accuracy of this CircleNotificationSubscription.

        Number of meters of acceptable error in tracking distance.  # noqa: E501

        :param tracking_accuracy: The tracking_accuracy of this CircleNotificationSubscription.
        :type tracking_accuracy: float
        """
        if tracking_accuracy is None:
            raise ValueError("Invalid value for `tracking_accuracy`, must not be `None`")  # noqa: E501

        self._tracking_accuracy = tracking_accuracy
