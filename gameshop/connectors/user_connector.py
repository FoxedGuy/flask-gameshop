from flask import abort
from gameshop.database import db
from gameshop.models.user import User


def create_new_user(login: str,
                    email: str):
    user = User.query.filter_by(login=login).first()
    if user is not None:
        abort(400, "User already exists.")
    user = User(login=login, email=email)
    db.session.add(user)
    db.session.commit()
    return user


def get_all_users():
    users = User.query.all()
    return users


def get_user_by_login(login: str):
    user = User.query.filter_by(login=login).first()
    if user is None:
        abort(404, "User doesn't exist")
    return user
