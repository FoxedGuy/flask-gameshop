from gameshop.database import db
from dataclasses import dataclass


@dataclass
class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    login: str = db.Column(db.String, unique=True, nullable=False)
    email: str = db.Column(db.String)
