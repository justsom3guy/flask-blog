from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.database.models import Blog, User


class BlogsApi(Resource):
    def get(self):
        blogs = Blog.objects().to_json()
        return Response(blogs, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=user_id)
        blog = Blog(**body, author=user)
        blog.save()
        user.update(push__blogs=blog)
        user.save()
        id = blog.id
        return {"id": str(id)}, 200


class BlogApi(Resource):
    @jwt_required
    def put(self, id):
        user_id = get_jwt_identity()
        blog = Blog.objects.get(id=id, author=user_id)
        body = request.get_json()
        Blog.objects.get(id=id).update(**body)
        return "", 200

    @jwt_required
    def delete(self, id):
        user_id = get_jwt_identity()
        blog = Blog.objects.get(id=id, author=user_id)
        movie.delete()
        return "", 200

    @jwt_required
    def get(self, id):
        blog = Blog.objects.get(id=id).to_json()
        return Response(blog, mimetype="application/json", status=200)

