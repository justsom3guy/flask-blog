from flask import Blueprint, render_template

home = Blueprint("home", __name__)


@home.route("/")
def login():
    return render_template("home.html")

