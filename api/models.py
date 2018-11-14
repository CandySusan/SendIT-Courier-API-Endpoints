
import random

parcel_inventory = {"parcels":[]}
user_list = {"users":[]}



class Order():
    def __init__(self, **args):

        self.pickup_location = args.get("pickup_location")
        self.destination = args.get("destination")
        self.date = args.get("date")
        self.sender = args.get("sender")
        self.sender_contact = args.get("sender_contact")
        self.receiver = args.get("receiver")
        self.receiver_contact = args.get("receiver_contact")
        self.weight = args.get("weight")
        self.parcelId = args.get("parcelId")
        self.userId = args.get("userId")

class User:
    def __init__(self, userId, username, password, email):
        self.userId = userId
        self.username = username
        self.email = email
        self.password = password    
 
    
   
    
