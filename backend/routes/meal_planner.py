from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from services import nutrislice.Nutrislice, nutrition.Nutrition

meal_planner = Blueprint('meal_planner', __name__)

# return current day's optimized meal plan
@meal_planner.route("/meal-plan", methods=["GET"])
@jwt_required
def get_optimized_meal():
    ns = Nutrislice()
    nt = Nutrition()

    menu = ns.fetch_menu()
    items = ns.clean_items()
    plan = greedy_optimizer()
    return jsonify(plan)

# return current day's menu options 
@meal_planner.route("/menu", methods=["GET"])
def get_meal_plan():
    pass
