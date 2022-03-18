from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

from backend.models import User
from backend.user import get_user
from backend.post import get_wall, create_post
from backend.consts import SUCCESS_CODE
from .strings import ERROR_MESSAGES


blueprint = Blueprint("views", __name__)


@blueprint.route("/")
@blueprint.route("/home")
def home():
    _, posts = get_wall()
    return render_template("home.html", posts=posts)


@blueprint.route("/<username>")
def user_page(username):
    error_code, user = get_user(username)
    if error_code == SUCCESS_CODE:
        error_code, posts = get_wall(username)
        if error_code == SUCCESS_CODE:
            return render_template("user_page.html", user=user, posts=posts)

    flash(ERROR_MESSAGES[error_code], category="error")
    return redirect(url_for("views.home"))