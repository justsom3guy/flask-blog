from config import Config
from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from app.database.db import initialize_db
from app.resources.routes import initialize_routes
from app.blueprints.bp import initialize_bp

app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config.from_object(Config)

initialize_db(app)
initialize_routes(api)
initialize_bp(app)
