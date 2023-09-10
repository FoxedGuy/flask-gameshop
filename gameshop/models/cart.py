from gameshop.database import db
from gameshop import ma


class Cart(db.Model):
    cart_id: int = db.Column(db.Integer, primary_key=True)


class CartSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Cart

    cart_id = ma.auto_field()
