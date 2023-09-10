from gameshop import app
from gameshop.connectors.user_connector import *
from gameshop.models.user import UserSchema
from flask import request


@app.get("/user/<int:user_id>")
async def get_user(user_id):
    user = get_user_by_index(user_id)
    user_schema = UserSchema(exclude=["password"])
    return user_schema.dump(user)


@app.put("/user/<int:user_id>")
async def update_user(user_id):
    data = request.json
    user_schema = UserSchema(exclude=["user_id"], partial=True)
    errors = user_schema.validate(data)
    if errors:
        abort(400, "Wrong request compared to given schema")

    user_schema = UserSchema(exclude=["password"])
    return user_schema.dump(update_user_by_index(user_id=user_id,
                                                 login=data.get("login"),
                                                 email=data.get("email"),
                                                 password=data.get("password")))


@app.get("/user/")
async def get_users():
    users = get_all_users()
    users_schema = UserSchema(exclude=["password"],
                              many=True)
    return users_schema.dump(users)


@app.post("/user/")
async def create_user():
    data = request.json
    user_schema = UserSchema(exclude=["user_id", "cart"])
    errors = user_schema.validate(data)
    if errors:
        abort(400)
    user_schema = UserSchema(exclude=["password"])
    return user_schema.dump(create_new_user(login=data.get("login"),
                                            email=data.get("email"),
                                            password=data.get("password")))


@app.delete("/user/<int:user_id>")
async def delete_user(user_id):
    delete_user_by_index(user_id)
    return "", 204
