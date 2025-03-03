from flask_restful import Resource
from instance.api import api
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash



class LoginAPI(Resource):
    def get(self):
        return {"message": "GET Function of Login API Triggered"}
    
    def post(self):
        print("Post request received")
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if username == "admin" and password == "admin#":
            return {"message": "Login Successful", 
                    "token" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30"} , 200
        return {"message": "Wrong Credentials"} , 401
    
    
api.add_resource(LoginAPI, '/login')