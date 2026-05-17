# main entry point of Flask app
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from models import User, UserProfile, CachedMenu
from extensions import db, bcrypt, jwt

from routes.auth import auth
from routes.meal_planner import meal_planner
from routes.profile import profile

import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

app.register_blueprint(auth)
app.register_blueprint(profile)
app.register_blueprint(meal_planner)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///nutrislice.db"
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

@app.route("/", methods=["GET"])
def home():
    return "App runs."

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)




