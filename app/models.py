from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from flask_avatars import Identicon

from app import db

class User(db.Model,UserMixin): #表名user
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    movies = db.relationship("Movie",back_populates="user")

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self,password):
        return check_password_hash(self.password_hash,password)


class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60)) # 电影标题
    year = db.Column(db.String(4))
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    timestamp = db.Column(db.DateTime,default = datetime.utcnow,index=True )
    user = db.relationship("User",back_populates="movies")
    avatar_s = db.Column(db.String(64))
    avatar_l = db.Column(db.String(64))
    avatar_m = db.Column(db.String(64))


    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)
        self.generate_avatar()


    def generate_avatar(self,):
        avatar = Identicon()
        filenames = avatar.generate(text=self.title)
        self.avatar_s = filenames[0]
        self.avatar_m = filenames[1]
        self.avatar_l = filenames[2]



    
