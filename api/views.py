from flask import Flask, jsonify, request, Response
import json
  
from api.models import Order,  parcel_inventory

app = Flask(__name__)



    
# re= [r"/^@.]+@[A-Za-z]+\.[a-z]+/"]

    
parcelId= ['1', '2', '3']

DeliveryOrder_dict =[{
	'1': {
		'PickUp Location': "PickUp_Location",
		'Destination': 1600,
		'Price': 1350, 
        'PaymentMode':"mm",
        'DeliveryDate':12/10/18,
        'Status':"delivered",
        'No Of Deliveries': 3

	},
	'2': {
		'PickUp Location': 1500,
		'Destination': 1600,
		'Price': 1350,
        'PaymentMode':"mm",
        'DeliveryDate':12/10/18,
        'Status':"delivered",
        'No Of Deliveries': 4

	},
    '003': {
		'PickUp Location': 1500,
		'Destination': 1600,
		'Price': 1350,
        'PaymentMode':"mm",
        'DeliveryDate':12/10/18,
        'Status': "delivered",
        'No Of Deliveries': 5
	},
}]


@app.route('/')
def Welcome():
    return "Welcome to SendIT Courier"

@app.route('/api/v1/login', methods=['POST'])
def login():
    info = request.get_json()

    username = info.get('username')
    password = info.get('password')

    if not username or username.isspace():
        return jsonify({
            'message': 'Enter a valid username.'
        }), 400
    if not password or password.isspace():
        return jsonify({
            'message': 'Enter a valid password.'
        }), 400


@app.route('/api/v1/signup', methods=['POST'])
def user_signup():
    info = request.get_json()

    username = info.get('username')
    email = info.get('email')
    password = info.get('password')


    if not username or username.isspace():
        return jsonify({'message': 'Username field can not be empty.'}), 400

    if not email or email.isspace():
        return jsonify({'message': 'Email field can not be empty.'}), 400
    # elif not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", email):
    #     return jsonify({'message': 'Enter a valid email address.'}), 400

    if not password or password.isspace():
        return jsonify({'message': 'Password field can not be left empty.'}), 400
    elif len(password) < 8:
        return jsonify({'message': 'Password must be at least 8 characters.'}), 400

#  Create parcel delivery order

@app.route('/api/v1/parcels', methods=["POST"])
def create_parcel_delivery_order():
    parcel = Order(PickUp_Location='PickUp_Location', Destination='Destination',
    Price='Price',Status='Status',PaymentMode='PaymentMode', No_Of_Deliveries='No_Of_Deliveries',Date='Date')           
    parcel.add_parcel_delivery_order(parcel)
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
        parcel_list.append(parcel.to_json())

    return jsonify({"parcel_inventory": parcel_list}), 200




#need authentication only admin can delete parcel
@app.route('/api/v1/parcels/<int:parcelId>', methods=['DELETE'])
def delete_parcel(parcelId):
	del parcel_inventory
	parcel_inventory.remove(parcelId)

	return jsonify({
		'message': parcelId + ' deleted successfully'
	}),200


   
