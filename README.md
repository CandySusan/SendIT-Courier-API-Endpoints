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
- To access and use the application's endpoints on Postman, Use the following URL []

# Application Features

	                      
|   EndPoint                     | Function        
| -------------                  |:-------------:
| GET /parcels                   |Fetch all parcel delivery orders 

| GET /parcels/<parcelId>        |Create a parcel delivery order  

| GET /users/<userId>/parcels    |Fetch all parcel delivery orders by a specific user

  PUT /parcels/<parcelId>/cancel |Cancel the specific parcel delivery order  

  POST /parcels                  |Create parcel delivery order
                
      

# Installation & Requirements;

- Python

- Flask (Python web framework)The following packages are optional:

- Markdown (optional) - Markdown support for the browsable API. 

- Pytest[Testing Framework]

- Install using pip: pip install Flask 

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
- Also used Stackoverflow to guide during building of api endpoints
- w3schools guided as well


# Author

Candy Susan

