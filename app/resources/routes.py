from .blogs import BlogApi, BlogsApi
from .auth import LoginApi, SignupApi


def initialize_routes(api):
    api.add_resource(BlogsApi, "/api/blogs")
    api.add_resource(BlogApi, "/api/blog/<id>")

    api.add_resource(SignupApi, "/api/auth/signup")
    api.add_resource(LoginApi, "/api/auth/login")

