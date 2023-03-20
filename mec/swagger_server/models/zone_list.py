# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.zone_info import ZoneInfo  # noqa: F401,E501
from swagger_server import util


class ZoneList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, resource_url: str=None, zone: List[ZoneInfo]=None):  # noqa: E501
        """ZoneList - a model defined in Swagger

        :param resource_url: The resource_url of this ZoneList.  # noqa: E501
        :type resource_url: str
        :param zone: The zone of this ZoneList.  # noqa: E501
        :type zone: List[ZoneInfo]
        """
        self.swagger_types = {
            'resource_url': str,
            'zone': List[ZoneInfo]
        }

        self.attribute_map = {
            'resource_url': 'resourceURL',
            'zone': 'zone'
        }
        self._resource_url = resource_url
        self._zone = zone

    @classmethod
    def from_dict(cls, dikt) -> 'ZoneList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ZoneList of this ZoneList.  # noqa: E501
        :rtype: ZoneList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resource_url(self) -> str:
        """Gets the resource_url of this ZoneList.

        Self referring URL  # noqa: E501

        :return: The resource_url of this ZoneList.
        :rtype: str
        """
        return self._resource_url

    @resource_url.setter
    def resource_url(self, resource_url: str):
        """Sets the resource_url of this ZoneList.

        Self referring URL  # noqa: E501

        :param resource_url: The resource_url of this ZoneList.
        :type resource_url: str
        """
        if resource_url is None:
            raise ValueError("Invalid value for `resource_url`, must not be `None`")  # noqa: E501

        self._resource_url = resource_url

    @property
    def zone(self) -> List[ZoneInfo]:
        """Gets the zone of this ZoneList.

        Collection of the zone information list.  # noqa: E501

        :return: The zone of this ZoneList.
        :rtype: List[ZoneInfo]
        """
        return self._zone

    @zone.setter
    def zone(self, zone: List[ZoneInfo]):
        """Sets the zone of this ZoneList.

        Collection of the zone information list.  # noqa: E501

        :param zone: The zone of this ZoneList.
        :type zone: List[ZoneInfo]
        """

        self._zone = zone
