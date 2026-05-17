from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import UserProfile
from extensions import db

profile = Blueprint('profile', __name__)


# route to save the user's metrics and goals
@profile.route("/profile", methods=["POST"])
@jwt_required()
def add_profile():
    user_id = get_jwt_identity()
    data = request.get_json()

    new_profile = UserProfile(
        user_id = user_id,
        age = data["age"],
        gender = data["gender"],
        height = data["height"],
        weight = data["weight"],
        activity_level = data["activity_level"],
        goal = data["goal"]
    )

    db.session.add(new_profile)
    db.session.commit()

    return jsonify(new_profile.to_dict()), 201

    """
    nutrition = Nutrition()
    user_bmr = nutrition.calculate_BMR(data["gender"], data["height"], data["weight"], data["age"])
    user_tdee = nutrition.calculate_TDEE(user_bmr, data["activity_level"])
    user_macros = nutrition.calculate_macros(user_tdee, data["goal"])

    return jsonify(user_macros)
    """


# route to get user's profile
@profile.route("/profile", methods=["GET"])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    profile = UserProfile.query.filter_by(user_id=user_id).first()

    if not profile:
        return jsonify({"Error" : "Profile not found"}), 404

    return jsonify({"User Metrics" : profile.to_dict()})
