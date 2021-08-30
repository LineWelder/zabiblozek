from flask import Flask, url_for

from extensions import *
from website import auth, views


def create_app():
    app = Flask(__name__, template_folder="website/templates")
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_manager.init_app(app)
    db.init_app(app)

    from backend.models import User
    db.create_all(app=app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    app.register_blueprint(views.blueprint)
    app.register_blueprint(auth.blueprint)

    return app