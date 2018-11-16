from flask import Flask, jsonify, request, Response
import json
import re
import uuid
from api.models import Order,  parcel_inventory, User, user_list
from api.controllers import Controller, User_controller
from flask_jwt_extended import(JWTManager,jwt_required,create_access_token,get_jwt_identity)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super_secret"
jwt = JWTManager(app)

controller = Controller()
user_controller = User_controller()


@app.route('/')
def Welcome():
    return "Welcome to SendIT Courier"


@app.route('/api/v1/auth/login',methods = ["POST"])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username != 'candy' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/api/v1/protected', methods=['GET'])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@app.route('/api/v1/auth/signup', methods=['POST'])
def signup():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    password_hash = generate_password_hash(password, method='sha256')

    if not username or username.isspace():
        return jsonify({'message': 'Username field can not be empty.'}), 400

    if not email or email.isspace():
        return jsonify({'message': 'Email field can not be empty.'}), 400
    elif not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", email):
        return jsonify({'message': 'Enter a valid email address.'}), 400

    if not password or password.isspace():
        return jsonify({'message': 'Password field can not be left empty.'}), 400
    elif len(password) < 8:
        return jsonify({'message': 'Password must be at least 8 characters.'}), 400




#  Create parcel delivery order,

@app.route('/api/v1/parcels', methods=["POST"])
@jwt_required
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
    status =data.get("status")
    order = Order(date=Date,pickup_location=Pickup_Location, destination=Destination,sender=Sender,
    sender_contact=Sender_Contact,receiver=Receiver,receiver_contact=Receiver_Contact,weight=Weight,
    parcelId=ParcelId,userId=UserId,status=status)
    controller.add_parcel_delivery_order(order)
    return jsonify({"message": "successfully added parcel",

    }), 201


# GET all parcels

@app.route('/api/v1/parcels', methods=["GET"])
@jwt_required
def get__all_parcels():
    parcels=controller.get_parcel_inventory()
    return jsonify(parcels),200


# GET specific parcel by id

@app.route('/api/v1/parcels/<int:parcelId>', methods=["GET"])
def get_specific_parcelId(parcelId):
    parcel=controller.get_parcel_by_parcelId(parcelId)

    return jsonify(parcel), 200

# Create users

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

#GET all users
@app.route('/api/v1/users', methods=['GET'])
def get_all_users():
    users=user_controller.get_users()
    return jsonify(users),200

# GET user with specific userId
@app.route('/api/v1/users/<int:userId>', methods=['GET'])
def get_user_with_specific_userId(userId):
    user=user_controller.get_user_by_userId(userId)
    return jsonify(user), 200
 
@app.route('/api/v1/users/<int:userId>/parcels', methods=['POST'])
def create_parcel_orders_by_specific_user(userId):
    order = request.get_json()
    for user in parcel_inventory.get("parcels"):
        if user.get("userId") == userId:
           new_parcel={
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

           user.get('parcels').append(new_parcel)
           return jsonify(new_parcel),201
    return jsonify({"message": "user not found"}),400


 
@app.route('/api/v1/users/<int:userId>/parcels', methods=['GET'])
def get_all_parcel_orders_by_specific_user(userId):
    for user in parcel_inventory.get("parcels"):
        if user.get("userId")==userId:
            return jsonify({"parcels":[]}),200
        return jsonify({"message":"User not found"})

@app.route('/api/v1/parcels/<int:parcelId>/cancel', methods=['PUT'])
def cancel_specific_order(parcelId):
    parcel=controller.cancel_specific_order_by_parcelId
    return jsonify(parcel),200


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message': 'The URL entered does not exist.'})