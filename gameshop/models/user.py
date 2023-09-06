from gameshop.database import db
from gameshop import ma


class User(db.Model):
    user_id: int = db.Column(db.Integer, primary_key=True)
    login: str = db.Column(db.String, unique=True, nullable=False)
    email: str = db.Column(db.String)
    password: str = db.Column(db.String)


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    user_id = ma.auto_field()
    login = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()
