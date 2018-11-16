import json
import unittest

import random

from api.models import Order, User

from api.views import app


class TestApi(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.hostname = "/api/v1/"
        self.parcels = {
            "date": "12/12/18",
            "pickup_location": "ntinda",
            "destination": "bunga",
            "sender": "picky",
            "sender_contact": "0789123456",
            "receiver": "mwamba",
            "receiver_contact": "075123456",
            "weight": "40kg",
            "parcelId": 2,
            "userId": 3,
            "status": "delivered"
        }

    def test_post_a_parcel(self):
        response = self.client.post(
            self.hostname+'parcels',
            content_type='application/json',
            data=json.dumps(self.parcels)
        )

        self.assertEqual(response.status_code, 201)

        

    def test_invalid_url(self):
        response = self.client.get(self.hostname)
        self.assertEqual(response.status_code, 404)

    def test_get_all_parcels(self):
        response = self.client.get(self.hostname + 'parcels')
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.status_code, 200)

    # def test_get_specific_parcel_by_parcelId(self):
    #     result = self.client.get(
    #         self.hostname + 'parcels'+ self.parcels.get("parcelId"))
    #     self.assertEqual(result.status_code, 200)

    def test_to_cancel_specific_parcel_delivery_order(self):
        response = self.client.put(self.hostname + 'parcels/1')
        self.assertEqual(response.status_code, 405)

    def test_get_invalid_parcel_delivery_orders(self):
        response = self.client.get(self.hostname+'parcels/0')

        self.assertEqual(response.status_code, 200)

    # def test_create_order_with_empty_destination(self):
    #     request = request.get_json()
    #     with self.assertRaises(ValueError):
    #         self.parcels(request['destination'] == ""
    #         orde
