from .consts import *
from .models import User


def get_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return ERROR_USER_NOT_FOUND, None
    return SUCCESS_CODE, user