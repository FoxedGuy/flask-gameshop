from flask import abort
from gameshop.database import db
from gameshop.models.user import User
from werkzeug.security import generate_password_hash


def create_new_user(login: str,
                    email: str,
                    password: str):
    user = User.query.filter_by(login=login).first()
    if user:
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
    if not user:
        abort(404, "User doesn't exist")
    return user


def update_user_by_index(user_id: int,
                         login: str = None,
                         email: str = None,
                         password: str = None):
    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        abort(400, "User wit this id doesn't exist")
    if login:
        user.login = login
    if email:
        user.email = email
    if password:
        user.password = generate_password_hash(password)

    db.session.commit()

    return user


def delete_user_by_index(user_id: int):
    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        abort(400, "User with given id doesn't exist")

    db.session.delete(user)
    db.session.commit()
