from flask import Blueprint

meal_planner = Blueprint('meal_planner', __name__)

@meal_planner.route("/meal-plan", methods=["GET"])
def get_meal_plan():
    menu = fetch_menu()
    items = clean_items()
    plan = greedy_optimizer()
    return jsonify(plan)

@meal_planner.route("/menu", methods=["POST"])
def get_meal():
    pass
