# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.security_info_o_auth2_info_grant_type import SecurityInfoOAuth2InfoGrantType  # noqa: F401,E501
from swagger_server import util


class SecurityInfoOAuth2Info(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, grant_types: List[SecurityInfoOAuth2InfoGrantType]=None, token_endpoint: str=None):  # noqa: E501
        """SecurityInfoOAuth2Info - a model defined in Swagger

        :param grant_types: The grant_types of this SecurityInfoOAuth2Info.  # noqa: E501
        :type grant_types: List[SecurityInfoOAuth2InfoGrantType]
        :param token_endpoint: The token_endpoint of this SecurityInfoOAuth2Info.  # noqa: E501
        :type token_endpoint: str
        """
        self.swagger_types = {
            'grant_types': List[SecurityInfoOAuth2InfoGrantType],
            'token_endpoint': str
        }

        self.attribute_map = {
            'grant_types': 'grantTypes',
            'token_endpoint': 'tokenEndpoint'
        }
        self._grant_types = grant_types
        self._token_endpoint = token_endpoint

    @classmethod
    def from_dict(cls, dikt) -> 'SecurityInfoOAuth2Info':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SecurityInfo.OAuth2Info of this SecurityInfoOAuth2Info.  # noqa: E501
        :rtype: SecurityInfoOAuth2Info
        """
        return util.deserialize_model(dikt, cls)

    @property
    def grant_types(self) -> List[SecurityInfoOAuth2InfoGrantType]:
        """Gets the grant_types of this SecurityInfoOAuth2Info.

        List of supported OAuth 2.0 grant types.  # noqa: E501

        :return: The grant_types of this SecurityInfoOAuth2Info.
        :rtype: List[SecurityInfoOAuth2InfoGrantType]
        """
        return self._grant_types

    @grant_types.setter
    def grant_types(self, grant_types: List[SecurityInfoOAuth2InfoGrantType]):
        """Sets the grant_types of this SecurityInfoOAuth2Info.

        List of supported OAuth 2.0 grant types.  # noqa: E501

        :param grant_types: The grant_types of this SecurityInfoOAuth2Info.
        :type grant_types: List[SecurityInfoOAuth2InfoGrantType]
        """
        if grant_types is None:
            raise ValueError("Invalid value for `grant_types`, must not be `None`")  # noqa: E501

        self._grant_types = grant_types

    @property
    def token_endpoint(self) -> str:
        """Gets the token_endpoint of this SecurityInfoOAuth2Info.

        The token endpoint  # noqa: E501

        :return: The token_endpoint of this SecurityInfoOAuth2Info.
        :rtype: str
        """
        return self._token_endpoint

    @token_endpoint.setter
    def token_endpoint(self, token_endpoint: str):
        """Sets the token_endpoint of this SecurityInfoOAuth2Info.

        The token endpoint  # noqa: E501

        :param token_endpoint: The token_endpoint of this SecurityInfoOAuth2Info.
        :type token_endpoint: str
        """
        if token_endpoint is None:
            raise ValueError("Invalid value for `token_endpoint`, must not be `None`")  # noqa: E501

        self._token_endpoint = token_endpoint
