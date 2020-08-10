from .user import user
from .home import home


def initialize_bp(app):
    app.register_blueprint(home)
    app.register_blueprint(user, url_prefix="/user")

