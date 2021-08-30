from extensions import db
from .models import User, Post
from .consts import *


def create_post(author_id, content):
    if not User.query.get(author_id):
        return ERROR_USER_NOT_FOUND, None

    if len(content) == 0:
        return ERROR_POST_EMPTY, None

    new_post = Post(
        author=author_id,
        content=content
    )
    db.session.add(new_post)
    db.session.commit()

    return SUCCESS_CODE, new_post


def get_wall(author=None):
    if author:
        user = User.query.filter_by(username=author).first()
        if not user:
            return ERROR_USER_NOT_FOUND, None

        return SUCCESS_CODE, user.posts
    
    return SUCCESS_CODE, Post.query.order_by(Post.date_created.desc()).all()