from gameshop import app
from gameshop.connectors.user_connector import *
from flask import request, jsonify, make_response


@app.get("/user")
async def get_user():
    data = request.json
    user = get_user_by_login(data['login'])
    return jsonify(user)


@app.get("/users")
async def get_users():
    users = get_all_users()
    return jsonify(users)


@app.post("/user")
async def create_user():
    data = request.json
    return jsonify(create_new_user(login=data.get("login"), email=data.get("email")))
