from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email


class SignUp(FlaskForm):
    first_name = StringField("Name", validators=[DataRequired()])
    user_name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    email = StringField(
        "Email", validators=[DataRequired(), Email(message="Enter a valid email")]
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(), EqualTo("confirm", message="Password must match")],
    )
    confirm = PasswordField("Repeat Password")
    submit = SubmitField("Sign up")


class Login(FlaskForm):
    user_name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

