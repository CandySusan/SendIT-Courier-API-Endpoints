from flask import Flask, jsonify, request, Response
import json
  
from api.models import Order,  parcel_inventory
from api.controllers import Controller
app = Flask(__name__)

controller = Controller()
users = [{
    "userId": 1,
    "username": "candy",
    "email": "candysusan55@gmail.com",
    "password":"golda@2020"

},
    {
    "userId": 2,
    "username": "picky",
    "email": "pickykimani@gmail.com",
    "password":"hawatuwezi"

}
]

orders= [
    {
    "Date":"12/10/17",
    "PickUp_Location":"Entebbe",
	"Destination":"Ntinda",
	"Sender":"Ziggy",
	"Sender_Contact":"07721234567",
    "Receiver":"07721234567",
    "Receiver_Contact":"07721234567",
    "Weight":"weight",
    "ParcelId":2,
    "UserId":1
    }	
]

specific_order=[]
    

@app.route('/')
def Welcome():
    return "Welcome to SendIT Courier"

#  Create parcel delivery order,

@app.route('/api/v1/parcels', methods=["POST"])
def create_parcel_delivery_order():
    data = request.get_json()
    Date = data.get("date")
    Pickup_Location = data.get("pickup_location")
    Destination = data.get("destination")
    Sender = data.get("sender")
    Sender_Contact = data.get("sender_contact")
    Receiver = data.get("receiver")
    Receiver_Contact = data.get("receiver_contact")
    Weight = data.get("weight")
    ParcelId = data.get("parcelId")
    UserId= data.get("userId")

    order = Order(date=Date,pickup_location=Pickup_Location, destination=Destination,sender=Sender,
    sender_contact=Sender_Contact,receiver=Receiver,receiver_contact=Receiver_Contact,weight=Weight,parcelId=ParcelId,userId=UserId)
    controller.add_parcel_delivery_order(order)

    return jsonify({"message": "successfully added parcel"}), 201


# GET all parcels
@app.route('/api/v1/parcels', methods=["GET"])

def get__all_parcels():

    parcels=controller.get_parcel_inventory()


    return jsonify(parcels),200


# GET specific parcel by id
@app.route('/api/v1/parcels/<int:parcelId>', methods=["GET"])
def get_specific_parcelId(parcelId):
    parcel=controller.get_parcel_by_parcelId(parcelId)

    return jsonify(parcel), 200




# Add users
@app.route('/api/v1/users', methods=['POST'])
def add_user():
    data = request.get_json()

    username = data.get("username")

    email = data.get("email")

    password = data.get("password")

    userId = len(users)+1 

    if not username or username.isspace():
        return jsonify({
            'message': 'Enter a valid username'
        }), 400
    if not password or password.isspace():
        return jsonify({
            'message': 'Enter a valid password'
        }), 400
    user = dict(
        username = username,
        email    = email,
        password = password
        )
    users.append(user)

    return jsonify({
            "message":"User added successfully",
            "user":user
        }),201

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    user_list = []
    for user in users:
        user_list.append(user.user_json())

    return jsonify({"users": user_list}), 200


@app.route('/api/v1/users/<int:userId>', methods=['GET'])
def get_user_with_specific_userId(userId):
    return next((item for item in orders
        if item(userId) == userId),False)

    if not userId or userId < 1:
        return jsonify({
            "message": "oops userId required and canot be less than one"
        }), 400

    for user in users:  # checking for a specific book
        if user["userId"] == userId:
            return jsonify({
                "user": user
            }), 200

    return jsonify({
        "message": " not found"
    }), 204   


 
       