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
    data = request.get_json()

    # find user by email
    user = User.query.filter_by(email = data["email"]).first()

    # check if email exists
    if (user == None):
        return jsonify({"Error": "Email doesn't exist"})
    
    # check if password matches the one in User db
    if not (bcrypt.check_password_hash(user.password_hash, data["password"])):
        return jsonify({"Error": "Password is incorrect"})

    # return JWT
    token = create_access_token(identity=user.id)
    return jsonify({"token" : token}), 200
    
    
    

