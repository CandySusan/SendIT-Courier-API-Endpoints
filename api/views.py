from flask import Flask, jsonify, request, Response
import json
  
from api.models import Order,  parcel_inventory, User, user_list
from api.controllers import Controller
from api.user_controller import User_controller
app = Flask(__name__)

controller = Controller()
user_controller = User_controller()


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
    userId = data.get("userId")
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    user = User(username=username,email=email,password=password,userId=userId)
    users = user_controller.add_user(user)
    return jsonify({
            "message":"User added successfully",
            "user": users
        }),201

@app.route('/api/v1/users', methods=['GET'])
def get_all_users():
    users=user_controller.get_users()


    return jsonify(users),200


@app.route('/api/v1/users/<int:userId>', methods=['GET'])
def get_user_with_specific_userId(userId):
    user=user_controller.get_user_by_userId(userId)

    return jsonify(user), 200

    

 
       