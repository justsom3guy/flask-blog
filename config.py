import os


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY")
    HOST = os.getenv("HOST")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_TOKEN_LOCATION = os.getenv("JWT_TOKEN_LOCATION")
    JWT_COOKIE_CSRF_PROTECT = os.getenv("JWT_COOKIE_CSRF_PROTECT")
