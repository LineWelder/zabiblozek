from flask import Blueprint
from flask_restful import Api, Resource

from .posts import PostList, Post


blueprint = Blueprint("api", __name__, url_prefix="/api/")
api = Api(blueprint)

api.add_resource(PostList, "/posts")
api.add_resource(Post, "/posts/<int:post_id>")