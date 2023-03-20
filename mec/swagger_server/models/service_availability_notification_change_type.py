# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ServiceAvailabilityNotificationChangeType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ADDED = "ADDED"
    REMOVED = "REMOVED"
    STATE_CHANGED = "STATE_CHANGED"
    ATTRIBUTES_CHANGED = "ATTRIBUTES_CHANGED"
    def __init__(self):  # noqa: E501
        """ServiceAvailabilityNotificationChangeType - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ServiceAvailabilityNotificationChangeType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ServiceAvailabilityNotification.ChangeType of this ServiceAvailabilityNotificationChangeType.  # noqa: E501
        :rtype: ServiceAvailabilityNotificationChangeType
        """
        return util.deserialize_model(dikt, cls)
