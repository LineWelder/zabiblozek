from flask_restful import Resource, abort
from flask_restful.reqparse import RequestParser
from flask_login import current_user
from sqlalchemy.sql import func

from backend import models
from backend.auth import check_login
from backend.consts import SUCCESS_CODE, ERROR_POST_ACCESS_DENIED
from backend.post import create_post, get_post, delete_post, edit_post
from website.strings import ERROR_MESSAGES


postlist_get_parser = RequestParser()
postlist_get_parser.add_argument("author")

post_parser = RequestParser()
post_parser.add_argument("username")
post_parser.add_argument("password")
post_parser.add_argument("content")


def error(error_code):
    abort(
        400,
        error_code=error_code,
        messsage=ERROR_MESSAGES[error_code]
    )


def backend_call(func, *args):
    error_code, value = func(*args)
    if error_code != SUCCESS_CODE:
        error(error_code)

    return value


def jsonify(post):
    return {
        "id": post.id,
        "author": post.user.username,
        "content": post.content,
        # "date_created": post.date_created # TODO solve the to-string conversion problem
    }


def login(args):
    if current_user.is_authenticated:
        return current_user

    return backend_call(check_login, args["username"], args["password"])


class PostList(Resource):
    def get(self):
        abort(405)

    def post(self):
        args = post_parser.parse_args()

        user = login(args)
        new_post = backend_call(create_post, user.id, args["content"])
        return jsonify(new_post)


class Post(Resource):
    def get(self, post_id):
        post = backend_call(get_post, post_id)

        return jsonify(post)

    def put(self, post_id):
        args = post_parser.parse_args()

        user = login(args)
        post = backend_call(get_post, post_id)

        if user.id != post.author:
            error(ERROR_POST_ACCESS_DENIED)

        edit_post(post_id, args["content"])
        return jsonify(post)

    def delete(self, post_id):
        args = post_parser.parse_args()

        user = login(args)
        post = backend_call(get_post, post_id)

        if user.id != post.author:
            error(ERROR_POST_ACCESS_DENIED)

        backend_call(delete_post, post_id)
        return "", 204