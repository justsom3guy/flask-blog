from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

home = Blueprint("home", __name__)


@home.route("/")
@home.route("/home")
def index():
    return render_template("index.html")


@home.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    return render_template("login.html")


@home.route("/sign-up")
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    return render_template("signup.html")
