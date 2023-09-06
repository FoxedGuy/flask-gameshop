from flask import abort
from gameshop.database import db
from gameshop.models.user import User, UserSchema
from werkzeug.security import generate_password_hash


def create_new_user(login: str,
                    email: str,
                    password: str):
    user = User.query.filter_by(login=login).first()
    if user is not None:
        abort(400, "User already exists.")
    user = User(login=login, email=email, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return user


def get_all_users():
    users = User.query.all()
    return users


def get_user_by_index(user_id: int):
    user = User.query.filter_by(user_id=user_id).first()
    if user is None:
        abort(404, "User doesn't exist")
    return user
