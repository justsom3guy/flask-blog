import datetime
from flask import request, Response
from flask_restful import Resource
from flask_jwt_extended import create_access_token, set_access_cookies
from flask_login import current_user, login_user
from app.database.models import User


class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {"id": str(id)}, 200


class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(email=body.get("email"))
        authorized = user.check_password(body.get("password"))
        if not authorized:
            return {"error": "Email or password invalid"}, 401

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        set_access_cookies(access_token)
        login_user(user)
        return {"token": access_token}
