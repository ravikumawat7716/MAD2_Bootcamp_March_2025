import os 
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, '.env'))

if os.getenv("DEBUG") == True:
    print(".env file is accessible by our application.")