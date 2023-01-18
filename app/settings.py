import sys
import os

from app import app

WIN = sys.platform.startswith("win")

if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

SQLALCHEMY_DATABASE_URI = prefix + os.path.join(os.path.dirname(app.root_path),"data.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.getenv("SECRET_KEY","secret_strings")
AVATARS_SAVE_PATH = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)),"uploads"),"avatars")


# flask内置变量:                 https://flask.palletsprojects.com/en/2.2.x/config/
# flask-sqlalchemy config keys: https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
