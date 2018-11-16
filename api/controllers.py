
from api.models import parcel_inventory
from api.models import user_list

class Controller:

    def add_parcel_delivery_order(self, order):
        """this function adds a parcel to the parcel_inventory"""
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
        
        parcel_inventory.append(parcel)
        return parcel_inventory
    
    def delete_parcel_delivery_order(self,parcelId):
        """This method removes the parcel order from a list using the parcelId"""
        parcel_inventory.remove(parcelId)

        return  parcel_inventory

    def get_parcel_by_parcelId(self,parcelId):
        """this method gets a parcel using the parcelId"""
        for parcel in parcel_inventory:
            if parcel["parcelId"] == parcelId:
                return parcel

    def cancel_specific_order_by_parcelId(self,parcelId):
        """this method cancels a specific order made by a  specific user"""
        request = request.get_json()
        parcel2 =[parcel for parcel in parcel_inventory.get("parcels") if parcel['parcelId'] == parcelId]
        parcel2[0]['status']= request["status"]
        return parcel2[0]


    def get_parcel_inventory(self):
        """this method returns the parcel_inventory"""
        return parcel_inventory

class User_controller:
    def add_user(self, user):
        new_user = {
            "userId":len(user_list)+1,
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




