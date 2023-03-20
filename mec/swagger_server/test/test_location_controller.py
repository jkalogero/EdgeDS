# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

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
from swagger_server.test import BaseTestCase


class TestLocationController(BaseTestCase):
    """LocationController integration test stubs"""

    def test_ap_by_id_get(self):
        """Test case for ap_by_id_get

        Radio Node Location Lookup
        """
        response = self.client.open(
            '/location/v2/queries/zones/{zoneId}/accessPoints/{accessPointId}'.format(zone_id='zone_id_example', access_point_id='access_point_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ap_get(self):
        """Test case for ap_get

        Radio Node Location Lookup
        """
        query_string = [('interest_realm', 'interest_realm_example')]
        response = self.client.open(
            '/location/v2/queries/zones/{zoneId}/accessPoints'.format(zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_area_circle_sub_delete(self):
        """Test case for area_circle_sub_delete

        Cancel a subscription
        """
        response = self.client.open(
            '/location/v2/subscriptions/area/circle/{subscriptionId}'.format(subscription_id='subscription_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_area_circle_sub_get(self):
        """Test case for area_circle_sub_get

        Retrieve subscription information
        """
        response = self.client.open(
            '/location/v2/subscriptions/area/circle/{subscriptionId}'.format(subscription_id='subscription_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_area_circle_sub_list_get(self):
        """Test case for area_circle_sub_list_get

        Retrieves all active subscriptions to area change notifications
        """
        response = self.client.open(
            '/location/v2/subscriptions/area/circle',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_area_circle_sub_post(self):
        """Test case for area_circle_sub_post

        Creates a subscription for area change notification
        """
        body = AreaCircleBody()
        response = self.client.open(
            '/location/v2/subscriptions/area/circle',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_area_circle_sub_put(self):
        """Test case for area_circle_sub_put

        Updates a subscription information
        """
        body = CircleSubscriptionIdBody()
        response = self.client.open(
            '/location/v2/subscriptions/area/circle/{subscriptionId}'.format(subscription_id='subscription_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_distance_get(self):
        """Test case for distance_get

        UE Distance Lookup of a specific UE
        """
        query_string = [('requester', 'requester_example'),
                        ('address', 'address_example'),
                        ('latitude', 3.4),
                        ('longitude', 3.4)]
        response = self.client.open(
            '/location/v2/queries/distance',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_distance_sub_delete(self):
        """Test case for distance_sub_delete

        Cancel a subscription
        """
        response = self.client.open(
            '/location/v2/subscriptions/distance/{subscriptionId}'.format(subscription_id='subscription_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_distance_sub_get(self):
        """Test case for distance_sub_get

        Retrieve subscription information
        """
        response = self.client.open(
            '/location/v2/subscriptions/distance/{subscriptionId}'.format(subscription_id='subscription_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_distance_sub_list_get(self):
        """Test case for distance_sub_list_get

        Retrieves all active subscriptions to distance change notifications
        """
        response = self.client.open(
            '/location/v2/subscriptions/distance',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_distance_sub_post(self):
        """Test case for distance_sub_post

        Creates a subscription for distance change notification
        """
        body = SubscriptionsDistanceBody()
        response = self.client.open(
            '/location/v2/subscriptions/distance',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_distance_sub_put(self):
        """Test case for distance_sub_put

        Updates a subscription information
        """
        body = DistanceSubscriptionIdBody()
        response = self.client.open(
            '/location/v2/subscriptions/distance/{subscriptionId}'.format(subscription_id='subscription_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_periodic_sub_delete(self):
        """Test case for periodic_sub_delete

        Cancel a subscription
        """
        response = self.client.open(
            '/location/v2/subscriptions/periodic/{subscriptionId}'.format(subscription_id='subscription_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_periodic_sub_get(self):
        """Test case for periodic_sub_get

        Retrieve subscription information
        """
        response = self.client.open(
            '/location/v2/subscriptions/periodic/{subscriptionId}'.format(subscription_id='subscription_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_periodic_sub_list_get(self):
        """Test case for periodic_sub_list_get

        Retrieves all active subscriptions to periodic notifications
        """
        response = self.client.open(
            '/location/v2/subscriptions/periodic',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_periodic_sub_post(self):
        """Test case for periodic_sub_post

        Creates a subscription for periodic notification
        """
        body = SubscriptionsPeriodicBody()
        response = self.client.open(
            '/location/v2/subscriptions/periodic',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_periodic_sub_put(self):
        """Test case for periodic_sub_put

        Updates a subscription information
        """
        body = PeriodicSubscriptionIdBody()
        response = self.client.open(
            '/location/v2/subscriptions/periodic/{subscriptionId}'.format(subscription_id='subscription_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_tracking_sub_delete(self):
        """Test case for user_tracking_sub_delete

        Cancel a subscription
        """
        response = self.client.open(
            '/location/v2/subscriptions/userTracking/{subscriptionId}'.format(subscription_id='subscription_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_tracking_sub_get(self):
        """Test case for user_tracking_sub_get

        Retrieve subscription information
        """
        response = self.client.open(
            '/location/v2/subscriptions/userTracking/{subscriptionId}'.format(subscription_id='subscription_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_tracking_sub_list_get(self):
        """Test case for user_tracking_sub_list_get

        Retrieves all active subscriptions to user tracking notifications
        """
        response = self.client.open(
            '/location/v2/subscriptions/userTracking',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_tracking_sub_post(self):
        """Test case for user_tracking_sub_post

        Creates a subscription for user tracking notification
        """
        body = SubscriptionsUserTrackingBody()
        response = self.client.open(
            '/location/v2/subscriptions/userTracking',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_tracking_sub_put(self):
        """Test case for user_tracking_sub_put

        Updates a subscription information
        """
        body = UserTrackingSubscriptionIdBody()
        response = self.client.open(
            '/location/v2/subscriptions/userTracking/{subscriptionId}'.format(subscription_id='subscription_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_get(self):
        """Test case for users_get

        UE Location Lookup of a specific UE or group of UEs
        """
        query_string = [('zone_id', 'zone_id_example'),
                        ('access_point_id', 'access_point_id_example'),
                        ('address', 'address_example')]
        response = self.client.open(
            '/location/v2/queries/users',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zonal_traffic_sub_delete(self):
        """Test case for zonal_traffic_sub_delete

        Cancel a subscription
        """
        response = self.client.open(
            '/location/v2/subscriptions/zonalTraffic/{subscriptionId}'.format(subscription_id='subscription_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zonal_traffic_sub_get(self):
        """Test case for zonal_traffic_sub_get

        Retrieve subscription information
        """
        response = self.client.open(
            '/location/v2/subscriptions/zonalTraffic/{subscriptionId}'.format(subscription_id='subscription_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zonal_traffic_sub_list_get(self):
        """Test case for zonal_traffic_sub_list_get

        Retrieves all active subscriptions to zonal traffic notifications
        """
        response = self.client.open(
            '/location/v2/subscriptions/zonalTraffic',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zonal_traffic_sub_post(self):
        """Test case for zonal_traffic_sub_post

        Creates a subscription for zonal traffic notification
        """
        body = SubscriptionsZonalTrafficBody()
        response = self.client.open(
            '/location/v2/subscriptions/zonalTraffic',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zonal_traffic_sub_put(self):
        """Test case for zonal_traffic_sub_put

        Updates a subscription information
        """
        body = ZonalTrafficSubscriptionIdBody()
        response = self.client.open(
            '/location/v2/subscriptions/zonalTraffic/{subscriptionId}'.format(subscription_id='subscription_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zone_status_sub_delete(self):
        """Test case for zone_status_sub_delete

        Cancel a subscription
        """
        response = self.client.open(
            '/location/v2/subscriptions/zoneStatus/{subscriptionId}'.format(subscription_id='subscription_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zone_status_sub_get(self):
        """Test case for zone_status_sub_get

        Retrieve subscription information
        """
        response = self.client.open(
            '/location/v2/subscriptions/zoneStatus/{subscriptionId}'.format(subscription_id='subscription_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zone_status_sub_list_get(self):
        """Test case for zone_status_sub_list_get

        Retrieves all active subscriptions to zone status notifications
        """
        response = self.client.open(
            '/location/v2/subscriptions/zoneStatus',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zone_status_sub_post(self):
        """Test case for zone_status_sub_post

        Creates a subscription for zone status notification
        """
        body = SubscriptionsZoneStatusBody()
        response = self.client.open(
            '/location/v2/subscriptions/zoneStatus',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zone_status_sub_put(self):
        """Test case for zone_status_sub_put

        Updates a subscription information
        """
        body = ZoneStatusSubscriptionIdBody()
        response = self.client.open(
            '/location/v2/subscriptions/zoneStatus/{subscriptionId}'.format(subscription_id='subscription_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zones_get(self):
        """Test case for zones_get

        Zones information Lookup
        """
        response = self.client.open(
            '/location/v2/queries/zones',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zones_get_by_id(self):
        """Test case for zones_get_by_id

        Zones information Lookup
        """
        response = self.client.open(
            '/location/v2/queries/zones/{zoneId}'.format(zone_id='zone_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
