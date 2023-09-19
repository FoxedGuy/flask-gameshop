from gameshop.connectors.user_connector import get_user_by_index
from gameshop.connectors.cart_connector import get_all_items_in_cart
from gameshop.connectors.item_connector import update_item_by_index
from gameshop.models.order import *
from flask import abort


def count_price(items_ic):
    price = 0
    for item_ic in items_ic:
        price += item_ic.item.price * item_ic.quantity

    return price


def create_new_order(user_id):
    user = get_user_by_index(user_id=user_id)
    items = get_all_items_in_cart(cart_id=user_id)
    if not user:
        abort(400, "User doesn't exist")

    order = Order(user_id=user_id, status="R", price=count_price(items))  # create empty order
    db.session.add(order)
    user.orders.append(order)
    for item in items:  # fill order with items from cart
        item_in_order = ItemInOrder(item_id=item.item.item_id,
                                    order_id=order.order_id,
                                    quantity=item.quantity,
                                    item=item.item)

        db.session.add(item_in_order)
        order.items.append(item_in_order)
        update_item_by_index(item_id=item_in_order.item_id,
                             quantity=item_in_order.item.quantity-item.quantity,
                             price=None,
                             item_name=None)

    db.session.add(order)
    db.session.commit()

    return order
