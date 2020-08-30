from mongoengine import connect


def initialize_db(app):
    connect(host=app.config["HOST"])

