from instance.api import api
from instance.app import app
from instance.database import db
from application import config



def create_app():
    api.init_app(app)
    app.app_context().push()

    
