from flask import Flask, Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import User
from extensions import bcrypt, db

auth = Blueprint('auth', __name__)

# add user into db and return JWT
@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # hash the password and add it to the User db
    hashed_pw = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
    new_account = User(
        email=data["email"], 
        password_hash=hashed_pw, 
        name=data["name"]
    )

    db.session.add(new_account)
    db.session.commit()

    token = create_access_token(identity=new_account.id)
    return jsonify({"token": token}), 201

# verify user credentials and return JWT
@auth.route('/login', methods=['POST'])
def login():
    pass

