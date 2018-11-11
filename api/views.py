from flask import Flask, jsonify, request, Response
import json
  
from api.models import Order,  parcel_inventory

app = Flask(__name__)

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
    "PickUpLocation":"Entebbe",
	"Destination":"Ntinda",
	"Price":20000,
	"Status": "Delivered",
	"PaymentMode": "cash",
	"No_Of_Deliveries":2,
	"OrderNumber":2,
	"quantity":4,
	"parcelId":2,
	"date":"12/20/16",
	 "item":[{
              "item_name" :"sandals",
              "weight":100,
             "size":[{
                    "lenth":10,
                    "height":2,
                    "width":5}]
                    }]
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
    print(data)
    print(data['OrderNumber'])
    print(data['Destination'])
    parcel = Order(data['OrderNumber'], data['Destination'], data['Price'],  data['Status'], 
    data['PaymentMode'], data['No_Of_Deliveries'], 
    data['PaymentMode'], data['quantity'], data['parcelId'], data['date'],data['item'])
    print(parcel)
    return jsonify({"message": "successfully added parcel with id"}), 201


# GET specific parcel by id
@app.route('/api/v1/parcels/<int:parcelId>', methods=["GET"])
def get_specific_parcelId(parcelId):
    for parcel in parcel_inventory:
        if parcel.parcelId ==  parcelId:
            return jsonify(parcel.to_json())

    return jsonify({"message": "oopsy parcel not found"}), 200


# GET all parcels
@app.route('/api/v1/parcels', methods=["GET"])

def get__all_parcels():
    parcel_list = []
    for parcel in parcel_inventory:
        parcel_list.append(parcel._json())

    return jsonify({"parcel_inventory": parcel_list}), 200

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


   