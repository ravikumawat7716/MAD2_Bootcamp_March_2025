from flask_restful import Resource
from instance.api import api
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token



class LoginAPI(Resource):
    def get(self):
        return {"message": "GET Function of Login API Triggered"}
    
    def post(self):
        print("Post request received")
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        if email == "rahul@test.com" and password == "admin":
            access_token = create_access_token(identity=email)
            return {"message": "Login Successful", 
                    "token" : access_token} , 200
        return {"message": "Wrong Credentials"} , 401
    

    
    
api.add_resource(LoginAPI, '/login')