from gameshop.database import db
from gameshop import ma


class Item(db.Model):
    item_id: int = db.Column(db.Integer, primary_key=True)
    item_name: str = db.Column(db.String, unique=True, nullable=False)
    quantity: int = db.Column(db.Integer)
    price: float = db.Column(db.Float)


class ItemSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Item

    item_id = ma.auto_field()
    item_name = ma.auto_field()
    quantity = ma.auto_field()
    price = ma.auto_field()
