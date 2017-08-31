from flask import render_template, redirect, url_for

from . import main
from app import db
from app.models import User


@main.route("/", methods=["GET"])
def index():
    return render_template("main/index.html")

@main.route("/users", methods=["GET"])
def users():
    users = db.session.query(User).all()
    return render_template("main/users.html", users=users)

@main.route("/users/<user_name>", methods=["GET"])
def new_user(user_name):
    try:
        user = User(username=user_name)
        db.session.add(user)
        db.session.commit()
    except Exception:
        db.session.rollback()
    return redirect(url_for("main.users"))