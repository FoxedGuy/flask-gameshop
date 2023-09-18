from gameshop import app
from gameshop.connectors.item_connector import *
from gameshop.models.item import ItemSchema
from flask import request


@app.post("/item/")
async def create_item():
    data = request.json
    item_schema = ItemSchema(exclude=["item_id"])
    errors = item_schema.validate(data)
    if errors:
        abort(400, "Wrong request compared to given schema")
    item_schema = ItemSchema()
    return item_schema.dump(create_new_item(item_name=data.get("item_name"),
                                            price=data.get("price"),
                                            quantity=data.get("quantity")))


@app.get("/item/<int:item_id>")
async def get_item(item_id):
    item_schema = ItemSchema()
    return item_schema.dump(get_item_by_index(item_id))


@app.get("/item/")
async def get_items():
    items_schema = ItemSchema(many=True)
    return items_schema.dump(get_all_items())


@app.put("/item/<int:item_id>")
async def update_item(item_id):
    data = request.json
    item_schema = ItemSchema(exclude=["item_id"], partial=True)
    errors = item_schema.validate(data)
    if errors:
        abort(400, "Wrong request compared to given schema")

    item_schema = ItemSchema()
    return item_schema.dump(update_item_by_index(item_id=item_id,
                                                 item_name=data.get("item_name"),
                                                 price=data.get("price"),
                                                 quantity=data.get("quantity")))


@app.delete("/item/<int:item_id>")
async def delete_item(item_id):
    delete_item_by_index(item_id)
    return "", 204
