from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Null, Nullable
from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            "id" : self.id,
            "email" : self.email,
            "password_hash": self.password_hash,
            "name" : self.name
        }


class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    activity_level = db.Column(db.String(50), nullable=False)
    goal = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id" : self.id,
            "user_id" : self.user_id,
            "age": self.age,
            "gender" : self.gender,
            "height" : self.height,
            "weight" : self.weight,
            "activitiy_level": self.activity_level,
            "goal" : self.goal,
        }


class CachedMenu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    meal_type = db.Column(db.String(50), nullable=False)
    menu_json = db.Column(db.JSON, nullable=False)

    def to_dict(self):
        return {
            "id" : self.id,
            "date" : self.date.isoformat(),
            "meal_type": self.meal_type,
            "menu_json" : self.menu_json
        }

 