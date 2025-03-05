from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from instance.api import api
from flask import request


class UserAPI(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        print("============================")
        print(current_user)
        print("============================")
        return {"message": f"GET Function of User API Triggered for {current_user}"}
    
api.add_resource(UserAPI, '/user')
    
        
        


