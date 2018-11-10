
import random
import datetime

parcel_inventory = []



class Order():
    def __init__(self,PickUp_Location, Destination,Price,Status,PaymentMode, No_Of_Deliveries,Date):

        self.PickUp_Location = PickUp_Location
        self.Destination = Destination
        self.Price = Price
        self.Status = Status
        self.PaymentMode = PaymentMode
        self.No_Of_Deliveries = No_Of_Deliveries
        self.OrderNumber = random.randint(0, 100)
        self.quantity = 10
        self.parcelId = random.randint(0, 100)
        self.Date = 12/20/17

    def add_parcel_delivery_order(self, parcelId):
        parcel_inventory.append(parcelId)

        return parcel_inventory
    
    def delete_parcel_delivery_order(self,parcelId):
        parcel_inventory.remove(parcelId)

        return  parcel_inventory

    def to_json(self):

        parcel_json = {
            "OrderNumber": self.OrderNumber,
            "PickUp_Location": self.PickUp_Location,
            "Destination": self.Destination,
            "Price": self.Price,
            "Status": self.Status,
            "PaymentMode": self.PaymentMode,
            "No_Of_Deliveries": self.No_Of_Deliveries,
            "quantity": self.quantity,
            "parcelId":self.parcelId,
            "date":self.Date

        }

        return parcel_json
        
    @staticmethod
    def get_parcel_inventory():
        return parcel_inventory

class User:
    def __init__(self, userId, username, password, email):
        self.userId = userId
        self.username = username
        self.email = email
        self.password = password    

    signup = [{
    "username": "candy",
    "email": "candysusan55@gmail.com",
    "password": "golda@2020"

}]  
    
    