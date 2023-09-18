from gameshop import app
from flask import request
from gameshop.models.cart import *
from gameshop.connectors.cart_connector import *


@app.post("/cart/<int:cart_id>")
async def add_item_to_cart(cart_id):
    data = request.json
    item_in_cart_s = ItemInCartSchema()
    return item_in_cart_s.dump(add_new_item_to_cart(cart_id=cart_id,
                                                    item_id=data.get("item_id"),
                                                    quantity=data.get("quantity")))


@app.get("/cart/<int:cart_id>/items/")
async def get_items_in_cart(cart_id):
    items = ItemInCartSchema(many=True)
    return items.dump(get_all_items_in_cart(cart_id=cart_id))


@app.delete("/cart/<int:cart_id>/items/")
async def delete_items_in_cart(cart_id):
    delete_all_items_in_cart(cart_id=cart_id)

    return "", 204
