from flask import Blueprint, render_template, flash, redirect, url_for
from backend.models import User


blueprint = Blueprint("views", __name__)


@blueprint.route("/")
@blueprint.route("/home")
def home():
    return render_template("home.html", users=User.query.all())


@blueprint.route("/<username>")
def user_page(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        flash(f"Strony @{username} nie ma", category="error")
        return redirect(url_for("views.home"))

    return render_template("user_page.html", user=user)