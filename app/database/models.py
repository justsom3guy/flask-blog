from mongoengine import Document, StringField, ReferenceField, ListField, PULL
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class Blog(Document):
    title = StringField(required=True)
    content = StringField()
    author = ReferenceField("User")


class User(UserMixin, Document):
    user_name = StringField(required=True, unique=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True, min_length=8)
    blogs = ListField(ReferenceField("Blog", reverse_delete_rule=PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def change_password(self, password):
        self.password = password
        self.hash_password()


@login.user_loader
def load_user(id):
    return User.objects.get(id=id)
