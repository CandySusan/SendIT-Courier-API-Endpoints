
from api.models import parcel_inventory
from api.models import user_list

class Controller:

    def add_parcel_delivery_order(self, order):
        parcel = {
            "date":order.date,
            "pickup_location":order.pickup_location,
            "destination":order.destination,
            "sender":order.sender,
            "sender_contact":order.sender_contact,
            "receiver":order.receiver,
            "receiver_contact":order.receiver_contact,
            "weight":order.weight,
            "parcelId":order.parcelId,
            "userId":order.userId,
            "status":order.status
        }
        
        parcel_inventory.get("parcels").append(parcel)

        return parcel_inventory
    
    def delete_parcel_delivery_order(self,parcelId):
        parcel_inventory.remove(parcelId)

        return  parcel_inventory

    def get_parcel_by_parcelId(self,parcelId):
        for parcel in parcel_inventory.get("parcels"):
            if parcel.get("parcelId") == parcelId:
                return parcel



    def get_parcel_inventory(self):
        return parcel_inventory

class User_controller:

    def add_user(self, user):
        new_user = {
            "userId":user.userId,
            "username":user.username,
            "email":user.email,
            "password":user.password,
          
        }
        
        user_list.get("users").append(new_user)

        return user_list
    
    def delete_user(self,userId):
        user_list.remove(userId)

        return  user_list

    def get_user_by_userId(self,userId):
        for user in user_list.get("users"):
            if user.get("userId") == userId:
                return user
           

    def get_users(self):
        return user_list