from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from models import UserProfile, CachedMenu
from services import Nutrislice, Nutrition, Optimizer
from datetime import date
import requests

meal_planner = Blueprint('meal_planner', __name__)

# return current day's optimized meal plan
@meal_planner.route("/meal-plan", methods=["GET"])
@jwt_required
def get_optimized_meal():
    # get user's profile
    user = get_jwt_identity()
    profile = UserProfile.query.filter_by(user_id = user).first()

    # calculate user's macros
    data = requests.get_json()
    ns = Nutrislice()
    nt = Nutrition()
    op = Optimizer()

    targets = nt.get_macros(data)

    # check if menu is in cache
    today = date.today()
    cached = CachedMenu.query.filter_by(date=today).first()

    if cached:
        menu = 
    else:
        menu = ns.fetch_menu()

    items = ns.clean_items()
    plan = op.greedy_optimizer()

    return jsonify(plan)

# return current day's menu options 
@meal_planner.route("/menu", methods=["GET"])
def get_meal_plan():
    pass
