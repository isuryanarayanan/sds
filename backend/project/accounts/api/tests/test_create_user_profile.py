"""
Testing the create user api endpoint.
"""
# Other imports
import json
from requests.auth import HTTPBasicAuth
# Django imports
from django.test import TestCase

from django.core.exceptions import ObjectDoesNotExist
# Rest framework imports
from rest_framework import status
from rest_framework.test import (
    APIRequestFactory,
    RequestsClient,
    APITestCase
)
# My imports
from accounts.models.user import User
from accounts.models.profiles import (
    customer,
    vendor,
    administrator
)


class CreateUserProfileTestCase(APITestCase):

    version = 'v1'
    host = '127.0.0.1'
    port = '8000'
    endpoint = f'/accounts/api/{version}/create_user_profile/'
    url = f'http://{host}:{port}{endpoint}'

    # Inorder for the test to run in order it is named
    # alphabetically increasing.

    def setUp(self):
        authorized_user = User.objects.create_user(
            'authorizedUser',
            'authorizedUser@gmail.com',
            3,
            'authorizedUser1',
        )

    def test_A_endpoint(self):
        # Making sure the endpoint works.
        print("\nRunning endpoint check (create_user_profile)")
        self.client.force_authenticate(
            User.objects.get(username='authorizedUser'))
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(f"Endpoint status {response.status_code}")

    def test_B_create_customer_profile(self):
        # The user creating the request
        customer_user = User.objects.create_user(
            'customerUser',
            'customerUser@gmail.com',
            1,
            'customerUser1',
        )
        # The profile params
        params = {
            "first_name": "customer",
            "last_name": "User"
        }
        self.client.force_authenticate(
            User.objects.get(username='customerUser'))
        response = self.client.post(self.url, params, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(customer.customer_profile.objects.get(
            user=User.objects.get(username="customerUser").id))
        print(f'Created user for {User.objects.get(username="customerUser")}')
