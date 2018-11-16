
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

    def cancel_specific_order_by_parcelId(self,parcelId):
        for parcel in parcel_inventory.get('parcels'): 
            parcel= parcel.add_parcel_delivery_order()
            if parcel.get('parcelId') == parcelId: 
                parcel['status']= "cancelled"
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




# class Delivered(Order):
# 	def __init__(self, **args):
# 		super().__init__( deadline,pay_extra)
# 		self.status = 'Delivered'
# 		self.pay_extra = pay_extra

# 	def check_status(self):
# 		return self.status

# 	def change_extra_dime(self, extra_dime):
# 		self.extra_dime = extra_dime


# class In_Transit(Order):
# 	def __init__(self, **args):
# 		super().__init__( deadline)
# 		self.status = 'In_Transit'
        

# 	def check_status(self):
# 		return self.status

#         delivered =[]

# def create_delivered(parcelId, deadline, pay_extra=None):
# 	if pay_extra < 20000:
# 		raise ValueError('Pay extra is less than 20000')
# 	if deadline > 24:
# 		raise ValueError('Parcel not yet delivered')
# 	order = Delivered(parcelId, deadline, pay_extra)
# 	delivered.append(order)


# def create_in_transit(parcelId, deadline):
# 	order = In_Transit(parcelId, deadline)
# 	delivered.append(order)

# 