from flask import Blueprint, render_template

user = Blueprint("user", __name__)


@user.route("/profile")
def profile():
    return render_template("profile.html")


@user.route("/login")
def login():
    return render_template("login.html")


@user.route("/sign-up")
def signup():
    return render_template("signup.html")


@user.route("/settings")
def settings():
    return render_template("settings.html")
