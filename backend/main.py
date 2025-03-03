from instance.app import app
from application import config
from utils.configuration import create_app
import api

create_app()

@app.route('/')
def home():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)