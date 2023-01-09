from flask import Flask
from flask_login import LoginManager
import os

#create app
app = Flask(__name__)
app.debug=True

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# Please note this is not at the top and is after creating "app"
from app import routes

#init LoginManager for app
login_manager = LoginManager(app)
login_manager.init_app(app)
#login_manager.login_view = 'login'

from app import user

#init and create database if necessary
from app import user_db
user_db.init_db()