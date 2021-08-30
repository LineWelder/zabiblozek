from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required

from backend.auth import check_login, register_user
from backend.consts import SUCCESS_CODE
from .strings import ERROR_MESSAGES


blueprint = Blueprint("auth", __name__)


@blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        error_code, user = check_login(username, password)
        if error_code == SUCCESS_CODE:
            login_user(user, remember=True)
            flash("Witajcie spowrotem!", category="success")
            return redirect(url_for("views.home"))
        else:
            flash(ERROR_MESSAGES[error_code], category="error")

    return render_template("login.html")


@blueprint.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        username = request.form.get("username")
        title = request.form.get("title")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        error_code, user = register_user(username, title, password1, password2)
        if error_code == SUCCESS_CODE:
            login_user(user, remember=True)
            flash("Witajcie!", category="success")
            return redirect(url_for("views.home"))
        else:
            flash(ERROR_MESSAGES[error_code], category="error")

    return render_template("signup.html")


@blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))