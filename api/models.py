
import random

parcel_inventory = []


class Order():
    def __init__(self, *args):

        self.PickUp_Location = args[0]
        self.Destination = args[1]
        self.Price = args[2]
        self.Status = args[3]
        self.PaymentMode = args[4]
        self.No_Of_Deliveries = args[5]
        self.OrderNumber = args[6]
        self.quantity = args[7]
        self.parcelId = args[8]
        self.Date = args[9]
        self.item  = args[10]

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
            "date":self.Date,
            "item":self.item

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
 
    
    def add_User(self):
        user_list.append(Users)
        if len(Users) == 0:
            UserId = 1

        else:
            for User in Users:
                x= user['userId']
                new_UserId = x+1
        
        return user_list



       
