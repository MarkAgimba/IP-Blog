from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager

@login manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index =True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    subscription = db.Column(db.Boolean)
    date_joined = db.Column(db.DateTime,default=datetime.utcnow)

    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    posts = db.relationship('Post',backref = 'post',lazy = "dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy='dynamic')

    