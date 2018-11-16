from flask import Flask, jsonify, request, Response
import json

import re

from api.models import user_list, parcel_inventory

class Validation:
    @staticmethod
    def validate_user_entered_empty_field(username,password,email):

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



    def get__all_user(userId):
        user={
            "username":"candy",
            "password":"test",
            "userId":len(user_list)+1
        }
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


    def validate_user_login(username,password):
        if not username or username.isspace():
                return jsonify({
                "message":"oops username required and cannot be empty"
                
                }),400
        
        if not password or password.isspace():
                return jsonify({
                   "message":"oops password required"
                }),400

    def validate_userId(userId,user):
        if type(userId) == int:
                return({
                "message": "oops userId should be a list"
                })

        if not user or len(user_list) == 0:
                return jsonify({
                "message":"oops user_list empty"
                }),400


    @staticmethod
    def validate_parcel(parcel):
        validations = []
       
        if not parcel['userId']:
            validations.append({'message':'userId is required'})
        else:
            if not isinstance(parcel['userIdd'], int):
                validations.append({'message':'Enter a valid userId'})

        if not parcel['receiver_contact'] or parcel['receiver'].isspace():
            validations.append({'message':' receiver is required'})
        

        return validations