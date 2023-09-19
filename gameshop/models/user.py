from gameshop.database import db
from gameshop import ma
from gameshop.models.cart import CartSchema
from gameshop.models.order import OrderSchema


class User(db.Model):
    user_id: int = db.Column(db.Integer, primary_key=True)
    login: str = db.Column(db.String, unique=True, nullable=False)
    email: str = db.Column(db.String)
    password: str = db.Column(db.String)
    cart_id = db.Column(db.Integer, db.ForeignKey("cart.cart_id"))
    cart = db.relationship("Cart")
    orders = db.relationship("Order")


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    user_id = ma.auto_field()
    login = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()
    cart_id = ma.auto_field()
    cart = ma.Nested(CartSchema)
    orders = ma.Nested(OrderSchema, many=True)
