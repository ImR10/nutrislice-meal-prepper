from flask import Blueprint

meal_planner = Blueprint('meal_planner', __name__)

# return current day's optimized meal plan
@meal_planner.route("/meal-plan", methods=["GET"])
def get_optimized_meal():
    menu = fetch_menu()
    items = clean_items()
    plan = greedy_optimizer()
    return jsonify(plan)

# return current day's menu options 
@meal_planner.route("/menu", methods=["GET"])
def get_meal_plan():
    pass
