from flask import Flask, jsonify, request, Response
import json

from api.models import user_list, parcel_inventory

class Validation:
    def validate_user_entered_empty_field(self):

        info = request.get_json()
    
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

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

    @app.route('/api/v1/users', methods=["GET"])
    def get__all_user():
        if not userId or userId < 1:
            return jsonify({
            "message": "oops userId required and canot be less than one"
        }), 400

        for user in user_list.get("users"):  
            if user.get("userId") == userId:
                return jsonify({
                    "user": user
            }), 200

        return jsonify({
            "message": "Book not found"
            }), 204

        for existing_user in user_list.get("users"):
            if existing_user.get("userId") == userId:
                return jsonify({
                "message":"User  exists"
            }),400


        @app.route('/api/v1/users', methods=['POST'])
        def add_user():
            data = request.get_json()
            userId = data.get("userId")
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            if not username or username.isspace():
                return jsonify({
                "message":"oops username required and cannot be empty"
                
                }),400
        
            if not password or password.isspace():
                return jsonify({
                   "message":"oops password required"
                }),400

            if type(userId) == int:
                return({
                "message": "oops userId should be a list"
                })

            if not user or len(book_authors) == 0:
                return jsonify({
                "message":"oops title required"
            }),400

            for user in user_list.get("users"):
                for single_user in user_list.get("users"):
                    if user.get("userId") != single_user.get("users"):
                        users.get("users").append(user)
