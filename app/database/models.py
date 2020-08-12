from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class Blog(db.Document):
    title = db.StringField(required=True)
    content = db.StringField()
    author = db.ReferenceField("User")


class User(UserMixin, db.Document):
    user_name = db.StringField(required=True, unique=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True, min_length=8)
    blogs = db.ListField(db.ReferenceField("Blog", reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def change_password(self, password):
        self.password = password
        self.hash_password()


@login.user_loader
def load_user(id):
    return User.objects.get(id=user_id)
