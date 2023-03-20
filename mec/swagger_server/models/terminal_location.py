# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.location_info import LocationInfo  # noqa: F401,E501
from swagger_server.models.retrieval_status import RetrievalStatus  # noqa: F401,E501
from swagger_server.models.service_error import ServiceError  # noqa: F401,E501
from swagger_server import util


class TerminalLocation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, address: str=None, current_location: LocationInfo=None, error_information: ServiceError=None, location_retrieval_status: RetrievalStatus=None):  # noqa: E501
        """TerminalLocation - a model defined in Swagger

        :param address: The address of this TerminalLocation.  # noqa: E501
        :type address: str
        :param current_location: The current_location of this TerminalLocation.  # noqa: E501
        :type current_location: LocationInfo
        :param error_information: The error_information of this TerminalLocation.  # noqa: E501
        :type error_information: ServiceError
        :param location_retrieval_status: The location_retrieval_status of this TerminalLocation.  # noqa: E501
        :type location_retrieval_status: RetrievalStatus
        """
        self.swagger_types = {
            'address': str,
            'current_location': LocationInfo,
            'error_information': ServiceError,
            'location_retrieval_status': RetrievalStatus
        }

        self.attribute_map = {
            'address': 'address',
            'current_location': 'currentLocation',
            'error_information': 'errorInformation',
            'location_retrieval_status': 'locationRetrievalStatus'
        }
        self._address = address
        self._current_location = current_location
        self._error_information = error_information
        self._location_retrieval_status = location_retrieval_status

    @classmethod
    def from_dict(cls, dikt) -> 'TerminalLocation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TerminalLocation of this TerminalLocation.  # noqa: E501
        :rtype: TerminalLocation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self) -> str:
        """Gets the address of this TerminalLocation.

        Address of the terminal to which the location information applies (e.g., 'sip' URI, 'tel' URI, 'acr' URI).  # noqa: E501

        :return: The address of this TerminalLocation.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this TerminalLocation.

        Address of the terminal to which the location information applies (e.g., 'sip' URI, 'tel' URI, 'acr' URI).  # noqa: E501

        :param address: The address of this TerminalLocation.
        :type address: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def current_location(self) -> LocationInfo:
        """Gets the current_location of this TerminalLocation.


        :return: The current_location of this TerminalLocation.
        :rtype: LocationInfo
        """
        return self._current_location

    @current_location.setter
    def current_location(self, current_location: LocationInfo):
        """Sets the current_location of this TerminalLocation.


        :param current_location: The current_location of this TerminalLocation.
        :type current_location: LocationInfo
        """

        self._current_location = current_location

    @property
    def error_information(self) -> ServiceError:
        """Gets the error_information of this TerminalLocation.


        :return: The error_information of this TerminalLocation.
        :rtype: ServiceError
        """
        return self._error_information

    @error_information.setter
    def error_information(self, error_information: ServiceError):
        """Sets the error_information of this TerminalLocation.


        :param error_information: The error_information of this TerminalLocation.
        :type error_information: ServiceError
        """

        self._error_information = error_information

    @property
    def location_retrieval_status(self) -> RetrievalStatus:
        """Gets the location_retrieval_status of this TerminalLocation.


        :return: The location_retrieval_status of this TerminalLocation.
        :rtype: RetrievalStatus
        """
        return self._location_retrieval_status

    @location_retrieval_status.setter
    def location_retrieval_status(self, location_retrieval_status: RetrievalStatus):
        """Sets the location_retrieval_status of this TerminalLocation.


        :param location_retrieval_status: The location_retrieval_status of this TerminalLocation.
        :type location_retrieval_status: RetrievalStatus
        """
        if location_retrieval_status is None:
            raise ValueError("Invalid value for `location_retrieval_status`, must not be `None`")  # noqa: E501

        self._location_retrieval_status = location_retrieval_status
