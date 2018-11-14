
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
 
    
   
    
class Validator:

    def auto_id(_list):
        global id
        if len(_list) == 0:
            id = len(_list) + 1
        else:
            id = id + 1
        return id

    def is_empty(item_list):
        if len(item_list) == 0:
            return True
        return False

    def doesnot_exist(item):
        if not item or len(item) == 0:
            return jsonify({
                'message': 'Sorry! Item should at least have three characters'
            }), 400

    def is_not_integer(item):
        if type(item) == int:
            return jsonify({
                'message': 'Sorry item should be an integer'
            }), 400

    def is_negative(item):
        if item in item_list:
            if item['item_id'] != item['item_id']:
                item_list.append(item)