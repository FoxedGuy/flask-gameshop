from gameshop.database import db
from gameshop.models.item import ItemSchema
from gameshop import ma


class ItemInCart(db.Model):
    item_id: int = db.Column(db.Integer, db.ForeignKey("item.item_id"), primary_key=True)
    cart_id: int = db.Column(db.Integer, db.ForeignKey("cart.cart_id"), nullable=False, primary_key=True)
    quantity: int = db.Column(db.Integer)
    item = db.relationship("Item")


class ItemInCartSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ItemInCart

    item_id = ma.auto_field()
    cart_id = ma.auto_field()
    quantity = ma.auto_field()
    item = ma.Nested(ItemSchema)


class Cart(db.Model):
    cart_id: int = db.Column(db.Integer, primary_key=True)
    items = db.relationship("ItemInCart", collection_class=list)


class CartSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Cart

    cart_id = ma.auto_field()
    items = ma.Nested(ItemInCartSchema, many=True)
