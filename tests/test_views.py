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
           "PickUp-Location":"entebbe",
            "Destination":"Ntinda",
            "Price":20000,
            "Status": "Delivered",
            "PaymentMode": "cash",
            "No_Of_Deliveries":2,
            "OrderNumber":2,
            "quantity":4,
            "parcelId":2,
            "date":"12/20/16",
            "item":[{
              "item_name" :
              [{"weight":10}],
             "size":[{
                    "lenth":10,
                    "height":2,
                    "width":5}]
                    }]
                }
                

    pending_userId = []
    generated_userId = [1,2,12.10]     
    

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
    
    def test_get_specific_parcel_by_parcelId(self):
        result = self.client.get(self.hostname + 'parcels'+str(self.parcels['parcelId']))
        self.assertEqual(result.status_code,200)
        # self.assertTrue(order.add_parcel_delivery_order(parcelId),True)
    def test_to_cancel_specific_parcel_delivery_order(self):
        response = self.client.put(self.hostname + 'parcels/1')
        self.assertEqual(response.status_code,405)

   

    def test_get_invalid_parcel_delivery_orders(self):
        response= self.client.get(self.hostname+'parcels/0')
       
        self.assertEqual(response.status_code, 200)

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

    # def test_user_login(self):
    #     users = {
    #         'username': 'candy',
    #         'email': 'candysusan55@gmail.com',
    #         'password': 'golda@2020'
    #     }
    #     response = self.client.post(self.hostname +'users',
    #         data=json.dumps(users)
    #     )
        
       
    #     self.assertEqual(response.status_code, 201)

    # def test_userId_mising(self):
    #     userId == 0
    
    #     self.assertEqual(get_user_with_specific_userId(userId),False)
    
    # def test_userId_is_int(self):
    #     userId = "str"
    #     self.assertFalse(get_user_with_specific_userId(userId),False)


    

   