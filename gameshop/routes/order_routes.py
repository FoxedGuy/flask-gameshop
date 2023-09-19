from gameshop.connectors.order_connector import *
from gameshop.connectors.cart_connector import delete_all_items_in_cart
from gameshop.models.order import OrderSchema
from gameshop import app
from flask import request


@app.post("/order/place")
def create_order():
    data = request.json
    order_schema = OrderSchema()
    new_order = create_new_order(user_id=data.get("user_id"))
    delete_all_items_in_cart(cart_id=data.get("user_id"))
    return order_schema.dump(new_order)
