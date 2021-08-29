from flask import url_for, current_app
from werkzeug.security import generate_password_hash, check_password_hash

from extensions import db
from models import User
from consts import *


def check_login(username, password):
    user = User.query.filter_by(username=username).first()

    if not user:
        return ERROR_AUTH_USERNAME_UNKNOWN, None
    if not check_password_hash(user.password, password):
        return ERROR_AUTH_PASSWORD_WRONG, None
    return SUCCESS_CODE, user


def _is_valid_username(username):
    return all(
        'a' <= ch <= 'z'
        or 'A' <= ch <= 'Z'
        or ch == '.'
        for ch in username
    )


def _has_no_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


def _conflicts_with_urls(username):
    return any(
        username == url_for(rule.endpoint, **(rule.defaults or {}))[1:]
        for rule in current_app.url_map.iter_rules()
        if "GET" in rule.methods and _has_no_params(rule)
    )


def register_user(username, title, password1, password2):
    username_exists = User.query.filter_by(username=username).first()

    if username_exists:
        return ERROR_AUTH_USERNAME_EXISTS, None
    if not _is_valid_username(username):
        return ERROR_AUTH_USERNAME_UNALLOWED_CHARACTERS, None
    if not 2 <= len(username) <= 30:
        return ERROR_AUTH_USERNAME_LENGTH, None
    if _conflicts_with_urls(username):
        return ERROR_AUTH_USERNAME_CONFLICTS, None

    if not 6 <= len(password1) < 30:
        return ERROR_AUTH_PASSWORD_LENGTH, None
    if password1 != password2:
        return ERROR_AUTH_PASSWORD_DO_NOT_MATCH, None

    if len(title) > 150:
        return ERROR_AUTH_TITLE_LENGTH, None
    if len(title) == 0:
        return ERROR_AUTH_TITLE_EMPTY, None

    new_user = User(
        username=username,
        title=title,
        password=generate_password_hash(password1)
    )
    db.session.add(new_user)
    db.session.commit()

    return SUCCESS_CODE, new_user