[![Coverage Status](https://coveralls.io/repos/github/CandySusan/SendIT-Courier-API-Endpoints/badge.svg?branch=develop)](https://coveralls.io/github/CandySusan/SendIT-Courier-API-Endpoints?branch=develop)
[![Build Status](https://travis-ci.org/CandySusan/SendIT-Courier-API-Endpoints.svg?branch=develop)](https://travis-ci.org/CandySusan/SendIT-Courier-API-Endpoints)
![Maintainability](https://api.codeclimate.com/v1/badges/5e1cc600d8edac9bbfd2/maintainability)


# SendIT Courier API Endpoints

SendIT Courier Api endpoints implements non-persistent data storage using data structures

# Project
********************************************************
To run the project Locally, clone [https://github.com/CandySusan/SendIT-Courier-API-Endpoints.git]

- cd into the folder that contains the cloned project.
- create a virtual environment.
- activate the virtual environment.
- pip install the requirements.txt.
- to run the project use python3. the run command is [python run.py].
- To access and use the application's endpoints on Postman, Use the following URL [https://courier-candy.herokuapp.com/]


# Application Features

	                      
|   EndPoint                        | Function        
| -------------                     |:-------------:
| GET /parcels                      |Fetch all parcel delivery orders 
| GET /parcels/parcelId             |Create a parcel delivery order  
| GET /users/userId/parcels         |Fetch all parcel delivery orders by a specific user
  PUT /parcels/parcelId/cancel      |Cancel the specific parcel delivery order  
  POST /parcels                     |Create parcel delivery order
                
      

# Installation & Requirements

- Python

- Flask (Python web framework)The following packages are optional:

- Markdown (optional) - Markdown support for the browsable API. 

- Pytest[Testing Framework]

- Install using pip: pip install Flask 

# Deployment

My app endpoints is hosted on heroku [https://courier-candy.herokuapp.com]

# An example on how to Use the endpoints

# Create a new parcel

Open postman and perform a POST request on [https://courier-candy.herokuapp.com/api/v1/parcels] Data should be in json format, e.g -
`{
    "parcels":[{"date":"12/12/18","destination":"bunga","parcelId":2,"pickup_location":"ntinda","receiver":"mwamba","receiver_contact":"075123456","sender":"picky","sender_contact":"0789123456","status":"delivered","userId":3,"weight":"40kg"}]
    
    }`   
Note:

All fields sould be filled for successful creation of a new parcel
 # Get all available parcels

Perform a GET request on [https://courier-candy.herokuapp.com/api/v1/parcels]

# Get a specific parcel by parcelId 
Perform a GET request and add parcelId as shown [https://courier-candy.herokuapp.com/api/v1/parcels/2] 

Note:

ParcelId is an integer and not a string so error message will be returned if string is entered instead.

# Import and initialization of my application:
*********************************************

from flask import Flask

app = Flask(__name__)

Setup Development Environment 

Install Python
Install Pip
Install VirtualEnv

# Running the tests

- Run pytest on the terminal to check for errors
- And also use the profeesional tool postman



# Acknowledgments

- Used this URL as a guideline to build the api endpoints [http://flask.pocoo.org/]
- Stackoverflow 
- w3schools


# Author

Candy Susan

