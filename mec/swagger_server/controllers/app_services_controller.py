import connexion
import six

from swagger_server.models.app_instance_id_services_body import AppInstanceIdServicesBody  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.models.service_info import ServiceInfo  # noqa: E501
from swagger_server import util
from swagger_server.utils import connector_db
from bson.json_util import dumps
import json
from flask_api import status
import requests


def app_services_get(app_instance_id, ser_instance_id=None, ser_name=None, ser_category_id=None, consumed_local_only=None, is_local=None, scope_of_locality=None):  # noqa: E501
    """get services

    This method retrieves information about a list of mecService resources. This method is typically used in \&quot;service availability query\&quot; procedure # noqa: E501

    :param app_instance_id: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
    :type app_instance_id: str
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
            "AppInstanceId": app_instance_id,
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
    

def app_services_post(body, app_instance_id):  # noqa: E501
    """create service

    This method is used to create a mecService resource. This method is typically used in \&quot;service availability update and new service registration\&quot; procedure # noqa: E501

    :param body: New ServiceInfo with updated &quot;state&quot; is included as entity body of the request
    :type body: dict | bytes
    :param app_instance_id: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
    :type app_instance_id: str

    :rtype: ServiceInfo
    """

    try:
        if connexion.request.is_json:
            body = AppInstanceIdServicesBody.from_dict(connexion.request.get_json())  # noqa: E501
        
        body['AppInstanceId'] = app_instance_id
        result = connector_db.postService(params=body)

        
        # get relevant MEC applications
        app_addresses = connector_db.getRelevantApps(service_category_id = result['serCategory']['id'])


        # notify relevant applications
        data = {
            'app_instance_id': app_instance_id,
            'service':{
                'service_id': result['serInstanceId'],
                'service_name': result['serName'],
                'app_instance_id': app_instance_id
            }

        }

        for address in app_addresses:
            r = requests.post(address+'service_notification', json=data)

        s = ServiceInfo()
        result = json.loads(dumps(s.from_dict(result).to_dict()))

    except Exception as e:
        raise Exception("An exception occurred :", e)
    return result


def app_services_service_id_delete(app_instance_id, service_id):  # noqa: E501
    """delete service

    This method deletes a mecService resource. This method is typically used in the service deregistration procedure.  # noqa: E501

    :param app_instance_id: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
    :type app_instance_id: str
    :param service_id: Represents a MEC service instance.
    :type service_id: str

    :rtype: None
    """
    try:
        params = {"serInstanceId": service_id, "AppInstanceId" :app_instance_id}
        del_result = connector_db.deleteService('ServiceInfo', params)
        if del_result.deleted_count == 0:
            return "The provided URI that cannot be mapped to a valid resource URI.", status.HTTP_404_NOT_FOUND

    except Exception as e:
        raise Exception("An exception occurred :", e)

    return '', status.HTTP_204_NO_CONTENT


def app_services_service_id_get(app_instance_id, service_id):  # noqa: E501
    """get service

    This method retrieves information about a mecService resource. This method is typically used in \&quot;service availability query\&quot; procedure # noqa: E501

    :param app_instance_id: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
    :type app_instance_id: str
    :param service_id: Represents a MEC service instance.
    :type service_id: str

    :rtype: ServiceInfo
    """
    try:
        params = {"serInstanceId": service_id, "AppInstanceId" :app_instance_id}
        serviceInfo = connector_db.getService('ServiceInfo', params)
        
        if serviceInfo is None:
            return "There are no registered services with the given parameters.", status.HTTP_404_NOT_FOUND
            
        s = ServiceInfo()
        result = json.loads(dumps(s.from_dict(serviceInfo).to_dict())) if serviceInfo is not None else {}

    except Exception as e:
        raise Exception("An exception occurred :", e)
    return result
