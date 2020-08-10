import os


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY")
    MONGO_HOST = os.getenv("MONGO_HOST")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    MONGODB_DB = os.getenv("MONGODB_DB")
