# main entry point of Flask app
from flask import Flask, request, jsonify
from models import User, UserProfile, CachedMenu

from routes.auth import auth
from routes.meal_planner import meal_planner
from routes.profile import profile

app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(profile)
app.register_blueprint(meal_planner)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///nutrislice.db"




