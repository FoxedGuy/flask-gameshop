from flask import Flask, jsonify
from gameshop.database import db
from werkzeug.exceptions import HTTPException
import json
import logging

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://db:db@db:5432/db"


@app.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


import gameshop.routes.user_routes


@app.route("/hello")
def hello_world():
    return "<p>Hello World!<p>"


logging.basicConfig(level=logging.INFO)
db.init_app(app)
with app.app_context():
    db.create_all()
