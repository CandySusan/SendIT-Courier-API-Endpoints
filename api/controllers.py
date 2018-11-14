
from api.models import parcel_inventory


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
            "weight":order.weight,~
            "parcelId":order.parcelId,
            "userId":order.userId
        }
        
        parcel_inventory.get("parcels").append(parcel)

        return parcel_inventory
    
    def delete_parcel_delivery_order(self,parcelId):
        parcel_inventory.remove(parcelId)

        return  parcel_inventory

    def get_parcel_by_parcelId(self,parcelId):
        for parcel in parcel_inventory.get("parcels"):# get access to list of parcels using the key
            if parcel.get("parcelId") == parcelId:
                return parcel



    def get_parcel_inventory(self):
        return parcel_inventory
