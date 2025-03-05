from instance.api import api
from instance.app import app
from instance.database import db
from application import config
from flask_jwt_extended import JWTManager
from flask_cors import CORS



def create_app():
    app.config["JWT_SECRET_KEY"] = "some-secret-key"
    api.init_app(app)
    JWTManager(app)
    CORS(app)
    app.app_context().push()

    
