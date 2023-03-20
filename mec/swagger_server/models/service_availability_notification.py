# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.service_availability_notification_service_references import ServiceAvailabilityNotificationServiceReferences  # noqa: F401,E501
from swagger_server.models.subscription import Subscription  # noqa: F401,E501
from swagger_server import util


class ServiceAvailabilityNotification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, notification_type: str=None, service_references: List[ServiceAvailabilityNotificationServiceReferences]=None, links: Subscription=None):  # noqa: E501
        """ServiceAvailabilityNotification - a model defined in Swagger

        :param notification_type: The notification_type of this ServiceAvailabilityNotification.  # noqa: E501
        :type notification_type: str
        :param service_references: The service_references of this ServiceAvailabilityNotification.  # noqa: E501
        :type service_references: List[ServiceAvailabilityNotificationServiceReferences]
        :param links: The links of this ServiceAvailabilityNotification.  # noqa: E501
        :type links: Subscription
        """
        self.swagger_types = {
            'notification_type': str,
            'service_references': List[ServiceAvailabilityNotificationServiceReferences],
            'links': Subscription
        }

        self.attribute_map = {
            'notification_type': 'notificationType',
            'service_references': 'serviceReferences',
            'links': '_links'
        }
        self._notification_type = notification_type
        self._service_references = service_references
        self._links = links

    @classmethod
    def from_dict(cls, dikt) -> 'ServiceAvailabilityNotification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ServiceAvailabilityNotification of this ServiceAvailabilityNotification.  # noqa: E501
        :rtype: ServiceAvailabilityNotification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def notification_type(self) -> str:
        """Gets the notification_type of this ServiceAvailabilityNotification.

        Shall be set to SerAvailabilityNotificationSubscription.  # noqa: E501

        :return: The notification_type of this ServiceAvailabilityNotification.
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type: str):
        """Sets the notification_type of this ServiceAvailabilityNotification.

        Shall be set to SerAvailabilityNotificationSubscription.  # noqa: E501

        :param notification_type: The notification_type of this ServiceAvailabilityNotification.
        :type notification_type: str
        """
        if notification_type is None:
            raise ValueError("Invalid value for `notification_type`, must not be `None`")  # noqa: E501

        self._notification_type = notification_type

    @property
    def service_references(self) -> List[ServiceAvailabilityNotificationServiceReferences]:
        """Gets the service_references of this ServiceAvailabilityNotification.


        :return: The service_references of this ServiceAvailabilityNotification.
        :rtype: List[ServiceAvailabilityNotificationServiceReferences]
        """
        return self._service_references

    @service_references.setter
    def service_references(self, service_references: List[ServiceAvailabilityNotificationServiceReferences]):
        """Sets the service_references of this ServiceAvailabilityNotification.


        :param service_references: The service_references of this ServiceAvailabilityNotification.
        :type service_references: List[ServiceAvailabilityNotificationServiceReferences]
        """
        if service_references is None:
            raise ValueError("Invalid value for `service_references`, must not be `None`")  # noqa: E501

        self._service_references = service_references

    @property
    def links(self) -> Subscription:
        """Gets the links of this ServiceAvailabilityNotification.


        :return: The links of this ServiceAvailabilityNotification.
        :rtype: Subscription
        """
        return self._links

    @links.setter
    def links(self, links: Subscription):
        """Sets the links of this ServiceAvailabilityNotification.


        :param links: The links of this ServiceAvailabilityNotification.
        :type links: Subscription
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links