from gameshop import db
from gameshop import ma
from gameshop.models.item import ItemSchema


class ItemInOrder(db.Model):
    order_id: int = db.Column(db.Integer, db.ForeignKey("order.order_id"), nullable=False, primary_key=True)
    item_id: int = db.Column(db.Integer, db.ForeignKey("item.item_id"), nullable=False)
    quantity: int = db.Column(db.Integer, nullable=False)
    item = db.relationship("Item")


class ItemInOrderSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ItemInOrder

    order_id = ma.auto_field()
    item_id = ma.auto_field()
    quantity = ma.auto_field()
    item = ma.Nested(ItemSchema)


class Order(db.Model):
    order_id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    status: str = db.Column(db.String, nullable=False)
    price: int = db.Column(db.Float, nullable=False)
    items = db.relationship("ItemInOrder", collection_class=list)


class OrderSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Order
    order_id = ma.auto_field()
    user_id = ma.auto_field()
    status = ma.auto_field()
    price = ma.auto_field()
    items = ma.Nested(ItemInOrderSchema, many=True)
