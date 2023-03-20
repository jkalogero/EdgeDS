# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.zone_info import ZoneInfo  # noqa: F401,E501
from swagger_server import util


class InlineResponse2003(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, zone_info: ZoneInfo=None):  # noqa: E501
        """InlineResponse2003 - a model defined in Swagger

        :param zone_info: The zone_info of this InlineResponse2003.  # noqa: E501
        :type zone_info: ZoneInfo
        """
        self.swagger_types = {
            'zone_info': ZoneInfo
        }

        self.attribute_map = {
            'zone_info': 'zoneInfo'
        }
        self._zone_info = zone_info

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2003':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_3 of this InlineResponse2003.  # noqa: E501
        :rtype: InlineResponse2003
        """
        return util.deserialize_model(dikt, cls)

    @property
    def zone_info(self) -> ZoneInfo:
        """Gets the zone_info of this InlineResponse2003.


        :return: The zone_info of this InlineResponse2003.
        :rtype: ZoneInfo
        """
        return self._zone_info

    @zone_info.setter
    def zone_info(self, zone_info: ZoneInfo):
        """Sets the zone_info of this InlineResponse2003.


        :param zone_info: The zone_info of this InlineResponse2003.
        :type zone_info: ZoneInfo
        """

        self._zone_info = zone_info
