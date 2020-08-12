from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, logout_user

user = Blueprint("user", __name__)


@user.route("/profile")
def profile():
    if not current_user.is_authenticated:
        return redirect(url_for("home.login"))
    return render_template("profile.html")


@user.route("/settings")
def settings():
    if not current_user.is_authenticated:
        return redirect(url_for("home.login"))
    return render_template("settings.html")


@user.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for("home.index"))

