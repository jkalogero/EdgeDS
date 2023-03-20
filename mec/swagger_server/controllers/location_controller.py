import connexion
import six

from swagger_server.models.area_circle_body import AreaCircleBody  # noqa: E501
from swagger_server.models.circle_subscription_id_body import CircleSubscriptionIdBody  # noqa: E501
from swagger_server.models.distance_subscription_id_body import DistanceSubscriptionIdBody  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response20010 import InlineResponse20010  # noqa: E501
from swagger_server.models.inline_response20011 import InlineResponse20011  # noqa: E501
from swagger_server.models.inline_response20012 import InlineResponse20012  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from swagger_server.models.inline_response2006 import InlineResponse2006  # noqa: E501
from swagger_server.models.inline_response2007 import InlineResponse2007  # noqa: E501
from swagger_server.models.inline_response2008 import InlineResponse2008  # noqa: E501
from swagger_server.models.inline_response2009 import InlineResponse2009  # noqa: E501
from swagger_server.models.periodic_subscription_id_body import PeriodicSubscriptionIdBody  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.models.subscriptions_distance_body import SubscriptionsDistanceBody  # noqa: E501
from swagger_server.models.subscriptions_periodic_body import SubscriptionsPeriodicBody  # noqa: E501
from swagger_server.models.subscriptions_user_tracking_body import SubscriptionsUserTrackingBody  # noqa: E501
from swagger_server.models.subscriptions_zonal_traffic_body import SubscriptionsZonalTrafficBody  # noqa: E501
from swagger_server.models.subscriptions_zone_status_body import SubscriptionsZoneStatusBody  # noqa: E501
from swagger_server.models.user_tracking_subscription_id_body import UserTrackingSubscriptionIdBody  # noqa: E501
from swagger_server.models.zonal_traffic_subscription_id_body import ZonalTrafficSubscriptionIdBody  # noqa: E501
from swagger_server.models.zone_status_subscription_id_body import ZoneStatusSubscriptionIdBody  # noqa: E501
from swagger_server import util
from swagger_server.models.user_info import UserInfo  # noqa: F401,E501
from swagger_server.utils import connector_db, compute_distance
from math import radians, cos, sin, asin, sqrt
from flask_api import status
from bson.json_util import dumps
import json
from flask import jsonify
from swagger_server.utils.define_problem import problem



def distance_get(address, requester=None, latitude=None, longitude=None):  # noqa: E501
    """UE Distance Lookup of a specific UE

    UE Distance Lookup between terminals or a terminal and a location # noqa: E501

    :param address: address of users (e.g. \&quot;sip\&quot; URI, \&quot;tel\&quot; URI, \&quot;acr\&quot; URI)
    :type address: List[str]
    :param requester: Entity that is requesting the information
    :type requester: str
    :param latitude: Latitude geo position
    :type latitude: float
    :param longitude: Longitude geo position
    :type longitude: float

    :rtype: InlineResponse200
    """
    
    if len(address) <= 2:
        try:
            # get lat and lon of UEs using their address
            usersInfo = connector_db.getResourceList('UserInfo', address=address)
            
            (latitude1, longitude1), *u2 = [(user['location']['latitude'], user['location']['longitude']) for user in usersInfo]
            
            if len(u2) == 1:
                latitude2, longitude2 = u2[0]
            elif u2 == [] and latitude is not None and longitude is not None:
                latitude2, longitude2 = latitude, longitude
            else:
                return "The provided address was not correct.", status.HTTP_400_BAD_REQUEST
            # compute distance
            distance =  compute_distance.compute_distance(latitude1, latitude2, longitude1, longitude2)
            
            # convert to `rtype`
            r = InlineResponse200()
            r.terminal_distance = {'distance': distance}

        except Exception as e:
            raise Exception("An exception occurred :", e)
    
    
    else:
        return "Incorrect parameters were passed to the request.", status.HTTP_400_BAD_REQUEST

    return r



def users_get(zone_id=None, access_point_id=None, address=None):  # noqa: E501
    """UE Location Lookup of a specific UE or group of UEs

    UE Location Lookup of a specific UE or group of UEs # noqa: E501

    :param zone_id: Identifier of zone
    :type zone_id: List[str]
    :param access_point_id: Identifier of access point
    :type access_point_id: List[str]
    :param address: address of users (e.g. \&quot;sip\&quot; URI, \&quot;tel\&quot; URI, \&quot;acr\&quot; URI)
    :type address: List[str]

    :rtype: InlineResponse2001
    """

    try:
        
        userList = connector_db.getResourceList('UserInfo', zoneId=zone_id, accessPointId=access_point_id, address=address)
        if len(userList) == 0:
            return problem()
        # convert to InlineResponse2001
        r = InlineResponse2001()
        r.user_list = {"user": userList, "resourceURL": "http://example.com/exampleAPI/location/v2/queries/users"}

    except Exception as e:
        raise Exception("An exception occurred :", e)
    
    # return r
    return json.loads(dumps(r.to_dict()))

def find_closest(address=None, latitude=None, longitude=None, user_type = ['user', 'device']):
    """
    Find the UE that is the closest to another UE or a location.

    :param address: address of users (e.g. \&quot;sip\&quot; URI, \&quot;tel\&quot; URI, \&quot;acr\&quot; URI)
    :type address: List[str]
    :param requester: Entity that is requesting the information
    :type requester: str
    :param latitude: Latitude geo position
    :type latitude: float
    :param longitude: Longitude geo position
    :type longitude: float
    :param user_type: Type of UE to search for
    :type user_type: string


    :rtype: InlineResponse2001
    """

    # get target location
    if address is not None:
        userInfo = connector_db.getResource('UserInfo', address=address)
        if userInfo is None:
            return problem()
        target_latitude, target_longitude = userInfo['location']['latitude'], userInfo['location']['longitude']

    elif latitude is not None and longitude is not None:
        target_latitude, target_longitude = latitude, longitude
    else:
        return "The provided address was not correct.", status.HTTP_400_BAD_REQUEST

    # retrieve all locations
    allUsers = connector_db.getResourceList('UserInfo', user_type=user_type)
    if len(allUsers) == 0:
        return problem()
    if address is not None:
        coordinates = [(user['location']['latitude'], user['location']['longitude'], user['_id']) for user in allUsers if user['address'] != address]
    else:
        coordinates = [(user['location']['latitude'], user['location']['longitude'], user['_id']) for user in allUsers]
    # compute distance from target
    distances = [(compute_distance.compute_distance(target_latitude, lat, target_longitude, lon), id) for (lat, lon, id) in coordinates]
    distances.sort() # it sorts by default on the first element of the tuple
    # select the closest UE
    closest_id = distances[0][1]
    closest_user = connector_db.getResource('UserInfo', _id=closest_id)
    # convert to InlineResponse2001
    r = InlineResponse2001()
    r.user_list = {"user": [closest_user], "resourceURL": "http://example.com/exampleAPI/location/v2/queries/users"}

    # return UserInfo
    return json.loads(dumps(r.to_dict()))


def find_close(address=None, latitude=None, longitude=None, distance=10, user_type = ['user', 'device']):
    """
    Find the UEs that are closer than `distance` to another UE or a location.

    :param address: address of users (e.g. \&quot;sip\&quot; URI, \&quot;tel\&quot; URI, \&quot;acr\&quot; URI)
    :type address: List[str]
    :param requester: Entity that is requesting the information
    :type requester: str
    :param latitude: Latitude geo position
    :type latitude: float
    :param longitude: Longitude geo position
    :type longitude: float
    :param distance: Distance geo position
    :type distance: float
    :param user_type: Type of UE to search for
    :type user_type: string

    :rtype: InlineResponse2001
    """
    # get target location
    if address is not None:
        userInfo = connector_db.getResource('UserInfo', address=address)
        if userInfo is None:
            return problem()
        target_latitude, target_longitude = userInfo['location']['latitude'], userInfo['location']['longitude']

    elif latitude is not None and longitude is not None:
        target_latitude, target_longitude = latitude, longitude
    else:
        return "The provided address was not correct.", status.HTTP_400_BAD_REQUEST

    # retrieve all locations
    allUsers = connector_db.getResourceList('UserInfo', user_type=user_type)
    if address is not None:
        coordinates = [(user['location']['latitude'], user['location']['longitude'], user['_id']) for user in allUsers if user['address'] != address]
    else:
        coordinates = [(user['location']['latitude'], user['location']['longitude'], user['_id']) for user in allUsers]
    # compute distance from target
    distances = [(compute_distance.compute_distance(target_latitude, lat, target_longitude, lon), id) for (lat, lon, id) in coordinates]
    # filter out the UEs that are more than `distance` away
    distances = [(d,id) for (d,id) in distances if d <= distance]

    distances.sort() # it sorts by default on the first element of the tuple
    
    ids = [id for (_,id) in distances]
    close_users = connector_db.getResourceList('UserInfo', _id=ids)
    # convert to InlineResponse2001
    r = InlineResponse2001()
    r.user_list = {"user": close_users, "resourceURL": "http://example.com/exampleAPI/location/v2/queries/users"}

    # return UserInfo
    return json.loads(dumps(r.to_dict()))
    



def zones_get():  # noqa: E501
    """Zones information Lookup

    Used to get a list of identifiers for zones authorized for use by the application. # noqa: E501


    :rtype: InlineResponse2002
    """
    try:
        
        zoneList = connector_db.getResourceList('ZoneInfo')
        if len(zoneList) == 0:
            return problem()
        # convert to InlineResponse2002
        r = InlineResponse2002()
        r.zone_list = {"zone": zoneList, "resourceURL": "http://example.com/exampleAPI/location/v2/queries/zones"}

    except Exception as e:
        raise Exception("An exception occurred :", e)
    
    # return r
    return json.loads(dumps(r.to_dict()))
    


def zones_get_by_id(zone_id):  # noqa: E501
    """Zones information Lookup

    Used to get the information for an authorized zone for use by the application. # noqa: E501

    :param zone_id: Indentifier of zone
    :type zone_id: str

    :rtype: InlineResponse2003
    """
    try:
        
        zoneInfo = connector_db.getResource('ZoneInfo', zoneId = zone_id)
        if len(zoneInfo) == 0:
            return problem()
        # convert to InlineResponse2003
        r = InlineResponse2003()
        r.zone_info = zoneInfo

    except Exception as e:
        raise Exception("An exception occurred :", e)
    
    # return r
    return json.loads(dumps(r.to_dict()))
