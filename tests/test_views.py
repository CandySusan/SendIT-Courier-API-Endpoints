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

             "OrderNumber": 7,
            "PickUp_Location": "ntinda",
            "Destination": "entebbe",
            "Price": 23000,
            "Status": "delivered",
            "PaymentMode": "cash",
            "No_Of_Deliveries": 4,
            "quantity": 8,
            "parcelId":1
        }
    

    def test_post_a_parcel(self):
        response = self.client.post(
            self.hostname+'parcels', data=json.dumps(self.parcels))

        self.assertEqual(response.status_code, 201)

    

    def test_invalid_url(self):
        response = self.client.get(self.hostname)
        self.assertEqual(response.status_code, 404)

    def test_get_all_parcels(self):
        response = self.client.get(self.hostname + 'parcels')
        self.assertEqual(response.status_code, 200)
    
    def test_get_specific_parcel_by_parcelId(self):
        result = self.client.get('/api/v1/parcels/'+str(self.parcels['parcelId']))
        self.assertEqual(result.status_code,200)
        # self.assertTrue(order.add_parcel_delivery_order(parcelId),True)

    # def test_parcelId_mising(self,parcelId): 
    #     order = Order(PickUp_Location='PickUp_Location', Destination='Destination',
    #     Price='Price',Status='Status',PaymentMode='PaymentMode',
    #     No_Of_Deliveries='No_Of_Deliveries',Date='Date', parcelId=1,)
    #     for parcel in Order.get_parcel_inventory():
    #         if parcel(parcelId) == 0:
    #             return parcelId
    #     self.assertEqual(Order.add_parcel_delivery_order(parcelId),False)
    
    # def test_parceId_is_int(self,parcelId):
    #     order = Order(PickUp_Location='PickUp_Location', Destination='Destination',
    #     Price='Price',Status='Status',PaymentMode='PaymentMode', 
    #     No_Of_Deliveries='No_Of_Deliveries',Date='Date')
    #     for parcel in Order.get_parcel_inventory():
    #         if type(parcelId) == int:
    #             return parcelId
        
    #     self.assertFalse(Order.add_parcel_delivery_order(parcelId),False)
    
    # def test_parcelId_exists(self,parcelId):
    #     parcelId = 1
    #     self.assertEqual(add_parcel_delivery_order(parcelId),True)

    # def test_input_is_integer(self,parcelId):
    #     if type(parcelId) == int:
    #         return parcelId
    #     self.assertTrue(add_parcel_delivery_order(parcelId),True)    

class TestUsers(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.hostname = "http://localhost:5000/api/v1/"

    # def test_user_signup(self):
    #     signup = {
    #         'username': 'candy',
    #         'email': 'candysusan55@gmail.com',
    #         'password': 'golda@2020'
    #     }
    #     response = self.client.post(
    #         'api/v1/signup',
    #         data=json.dumps(signup)
    #     )
    #     message = json.loads(response.data.decode())

    #     self.assertEqual(message['message'],
    #                      'SignUp successfull')
    #     self.assertEqual(response.status_code, 201)

    # def test_email_field_empty(self):
    #     signup = {
    #         'username': 'candy',
    #         'email': '',
    #         'password': 'golda@2020'
    #     }
    #     response = self.client.post(
    #         'api/v1/signup',
    #         data=json.dumps(signup)
    #     )
    #     message = json.loads(response.data.decode())

    #     self.assertEqual(message['message'],
    #                      'Email field can not be empty!.')

    # def test_user_entered_wrong_password(self):
	# 	    with self.assertRaises(ValueError):
	# 		    signup = dict({
    #             'username':'candy',
    #             'eamil':'candysusan55@gmail.com',
    #             'password':'candysusan'
    #         })