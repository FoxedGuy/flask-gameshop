from gameshop.database import db
from gameshop import ma
from flask_marshmallow import fields
from gameshop.models.cart import Cart, CartSchema


class User(db.Model):
    user_id: int = db.Column(db.Integer, primary_key=True)
    login: str = db.Column(db.String, unique=True, nullable=False)
    email: str = db.Column(db.String)
    password: str = db.Column(db.String)
    cart_id = db.Column(db.Integer, db.ForeignKey("cart.cart_id"))
    cart = db.relationship("Cart")


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    user_id = ma.auto_field()
    login = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()
    cart_id = ma.auto_field()
    cart = ma.Nested(CartSchema)
