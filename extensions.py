from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path

from website.strings import LOGIN_MESSAGE


login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = LOGIN_MESSAGE
login_manager.login_message_category = "error"


db = SQLAlchemy()