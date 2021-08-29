from flask import Blueprint, render_template, flash, redirect, url_for
from models import User


views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html", users=User.query.all())


@views.route("/<username>")
def user_page(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        flash(f"Strony @{username} nie ma", category="error")
        return redirect(url_for("views.home"))

    return render_template("user_page.html", user=user)