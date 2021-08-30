from flask_login import UserMixin
from sqlalchemy.sql import func

from extensions import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    title = db.Column(db.String(150))
    password = db.Column(db.String(102))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())