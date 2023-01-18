from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
from flask_avatars import Avatars


app = Flask(__name__)
app.config.from_pyfile("settings.py")
db = SQLAlchemy(app)
bootstrap = Bootstrap5(app)
avatars = Avatars(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

from app import commands,views,models,errors
from app.models import User,Movie

@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)


@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    return user






