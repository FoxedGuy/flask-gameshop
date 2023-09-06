from gameshop import app
from gameshop.connectors.user_connector import *
from gameshop.models.user import UserSchema
from flask import request, jsonify


@app.get("/user/<int:user_id>")
async def get_user(user_id):
    user = get_user_by_index(user_id)
    user_schema = UserSchema(exclude=["password"])
    return user_schema.dump(user)


@app.get("/user/")
async def get_users():
    users = get_all_users()
    users_schema = UserSchema(exclude=["password"],
                              many=True)
    return users_schema.dump(users)


@app.post("/user/")
async def create_user():
    data = request.json
    user_schema = UserSchema(exclude=["user_id"])
    errors = user_schema.validate(data)
    if errors:
        abort(400)
    user_schema = UserSchema(exclude=["password"])
    return user_schema.dump(create_new_user(login=data.get("login"),
                                            email=data.get("email"),
                                            password=data.get("password")))
