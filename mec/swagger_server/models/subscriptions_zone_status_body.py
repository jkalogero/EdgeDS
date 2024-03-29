# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.zone_status_subscription import ZoneStatusSubscription  # noqa: F401,E501
from swagger_server import util


class SubscriptionsZoneStatusBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, zone_status_subscription: ZoneStatusSubscription=None):  # noqa: E501
        """SubscriptionsZoneStatusBody - a model defined in Swagger

        :param zone_status_subscription: The zone_status_subscription of this SubscriptionsZoneStatusBody.  # noqa: E501
        :type zone_status_subscription: ZoneStatusSubscription
        """
        self.swagger_types = {
            'zone_status_subscription': ZoneStatusSubscription
        }

        self.attribute_map = {
            'zone_status_subscription': 'zoneStatusSubscription'
        }
        self._zone_status_subscription = zone_status_subscription

    @classmethod
    def from_dict(cls, dikt) -> 'SubscriptionsZoneStatusBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The subscriptions_zoneStatus_body of this SubscriptionsZoneStatusBody.  # noqa: E501
        :rtype: SubscriptionsZoneStatusBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def zone_status_subscription(self) -> ZoneStatusSubscription:
        """Gets the zone_status_subscription of this SubscriptionsZoneStatusBody.


        :return: The zone_status_subscription of this SubscriptionsZoneStatusBody.
        :rtype: ZoneStatusSubscription
        """
        return self._zone_status_subscription

    @zone_status_subscription.setter
    def zone_status_subscription(self, zone_status_subscription: ZoneStatusSubscription):
        """Sets the zone_status_subscription of this SubscriptionsZoneStatusBody.


        :param zone_status_subscription: The zone_status_subscription of this SubscriptionsZoneStatusBody.
        :type zone_status_subscription: ZoneStatusSubscription
        """

        self._zone_status_subscription = zone_status_subscription
