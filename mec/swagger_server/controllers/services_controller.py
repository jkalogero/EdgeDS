import connexion
import six

from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.models.service_info import ServiceInfo  # noqa: E501
from swagger_server import util
from swagger_server.utils import connector_db, compute_distance
import json
from json import dumps
from flask_api import status


def services_get(ser_instance_id=None, ser_name=None, ser_category_id=None, consumed_local_only=None, is_local=None, scope_of_locality=None):  # noqa: E501
    """get services

    This method retrieves information about a list of mecService resources. This method is typically used in \&quot;service availability query\&quot; procedure # noqa: E501

    :param ser_instance_id: A MEC application instance may use multiple ser_instance_ids as an input parameter to query the availability of a list of MEC service instances. Either \&quot;ser_instance_id\&quot; or \&quot;ser_name\&quot; or \&quot;ser_category_id\&quot; or none of them shall be present.
    :type ser_instance_id: List[str]
    :param ser_name: A MEC application instance may use multiple ser_names as an input parameter to query the availability of a list of MEC service instances. Either \&quot;ser_instance_id\&quot; or \&quot;ser_name\&quot; or \&quot;ser_category_id\&quot; or none of them shall be present.
    :type ser_name: List[str]
    :param ser_category_id: A MEC application instance may use ser_category_id as an input parameter to query the availability of a list of MEC service instances in a serCategory. Either \&quot;ser_instance_id\&quot; or \&quot;ser_name\&quot; or \&quot;ser_category_id\&quot; or none of them shall be present.
    :type ser_category_id: str
    :param consumed_local_only: Indicate whether the service can only be consumed by the MEC  applications located in the same locality (as defined by  scopeOfLocality) as this service instance.
    :type consumed_local_only: bool
    :param is_local: Indicate whether the service is located in the same locality (as  defined by scopeOfLocality) as the consuming MEC application.
    :type is_local: bool
    :param scope_of_locality: A MEC application instance may use scope_of_locality as an input  parameter to query the availability of a list of MEC service instances  with a certain scope of locality.
    :type scope_of_locality: str

    :rtype: List[ServiceInfo]
    """
    params = {
        "multiple": {
            "serInstanceId": ser_instance_id,
            "serName": ser_name
        },
        "single": {
            "serCategory.id": ser_category_id,
            "scopeOfLocality": scope_of_locality,
            "consumedLocalOnly": consumed_local_only,
            "isLocal": is_local
        }
    }
    try:
        serviceInfo = connector_db.getServices('ServiceInfo', params)
        if len(serviceInfo) == 0:
            return "There are no registered services with the given parameters.", status.HTTP_404_NOT_FOUND
        s = ServiceInfo()
        result = [json.loads(dumps(s.from_dict(service).to_dict())) for service in serviceInfo]
    
    except Exception as e:
            raise Exception("An exception occurred :", e)
    
    return result


def services_service_id_get(service_id):  # noqa: E501
    """get service

    This method retrieves information about a mecService resource. This method is typically used in \&quot;service availability query\&quot; procedure # noqa: E501

    :param service_id: Represents a MEC service instance.
    :type service_id: str

    :rtype: ServiceInfo
    """

    try:
        params = {"serInstanceId": service_id}
        serviceInfo = connector_db.getService('ServiceInfo', params)
        
        if serviceInfo is None:
            return "There are no registered services with the given parameters.", status.HTTP_404_NOT_FOUND
            
        s = ServiceInfo()
        result = json.loads(dumps(s.from_dict(serviceInfo).to_dict())) if serviceInfo is not None else {}

    except Exception as e:
        raise Exception("An exception occurred :", e)
    return result