from gameshop.database import db
from werkzeug.exceptions import HTTPException
from gameshop.models.user import User


def create_new_user(login: str,
                    email: str):
    user = User.query.filter_by(login=login).first()
    if user is not None:
        raise HTTPException(description="User already exists!")
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
        raise HTTPException(description="User don't exist")
    return user
