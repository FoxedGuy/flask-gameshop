from flask import abort
from gameshop.database import db
from gameshop.models.item import Item


def create_new_item(item_name: str,
                    price: float,
                    quantity: int):
    item = Item.query.filter_by(item_name=item_name).first()

    if item:
        abort(400, "Item already exists")

    item = Item(item_name=item_name,
                price=price,
                quantity=quantity)

    db.session.add(item)
    db.session.commit()

    return item


def get_item_by_index(item_id: int):
    item = Item.query.filter_by(item_id=item_id).first()

    if not item:
        abort(400, "Item doesn't exist")

    return item


def get_all_items():
    return Item.query.all()


def update_item_by_index(item_id: int,
                         item_name: str | None,
                         price: float | None,
                         quantity: int | None):
    item = Item.query.filter_by(item_id=item_id).first()

    if not item:
        abort(400, "Item doesn't exist")

    if item_name:
        item.item_name = item_name
    if price:
        item.price = price
    if quantity:
        item.quantity = quantity

    db.session.commit()

    return item


def delete_item_by_index(item_id: int):
    item = Item.query.filter_by(item_id=item_id).first()

    if not item:
        abort(400, "Item doesn't exist")

    db.session.delete(item)
    db.session.commit()
