from flask import abort
from gameshop.database import db
from gameshop.models.item import Item
from gameshop.models.cart import Cart, ItemInCart


def create_new_cart():
    cart = Cart()

    db.session.add(cart)
    db.session.commit()

    return cart


def delete_cart(cart_id: int):
    cart = Cart.query.filter_by(cart_id=cart_id).first()
    items = ItemInCart.query.filter_by(cart_id=cart_id).all()
    if not cart:
        abort(400)

    db.session.delete(items)
    db.session.delete(cart)
    db.session.commit()

    return "", 204


def delete_all_items_in_cart(cart_id: int):
    ItemInCart.query.filter_by(cart_id=cart_id).delete()
    db.session.commit()


def add_new_item_to_cart(cart_id: int,
                         item_id: int,
                         quantity: int):
    itemic = ItemInCart.query.filter_by(cart_id=cart_id, item_id=item_id).first()
    item = Item.query.filter_by(item_id=item_id).first()

    if itemic:
        if itemic.quantity + quantity > item.quantity:
            abort(400, "Reached the product limit")
        itemic.quantity += quantity
        db.session.commit()
        return itemic

    cart = Cart.query.filter_by(cart_id=cart_id).first()
    itemic = ItemInCart(item_id=item_id, cart_id=cart_id, item=item, quantity=quantity)
    db.session.add(itemic)
    cart.items.append(itemic)
    db.session.commit()

    return itemic


def get_all_items_in_cart(cart_id: int):
    cart = Cart.query.filter_by(cart_id=cart_id).first()
    if not cart:
        abort(400, "No cart with given id")

    return cart.items
