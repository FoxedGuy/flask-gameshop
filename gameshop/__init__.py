from flask import Flask
from gameshop.database import db
import logging

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://db:db@db:5432/db"

import gameshop.routes.user_routes


@app.route("/hello")
def hello_world():
    return "<p>Hello World!<p>"


logging.basicConfig(level=logging.INFO)
db.init_app(app)
with app.app_context():
    db.create_all()
