from flask import Blueprint

profile = Blueprint('profile', __name__)

# route to get user's profile
@profile.route("/profile", methods=["GET"])
def get_profile():
    pass

# route to save the user's metrics and goals
@profile.route("/profile", methods=["POST"])
def add_profile():
    pass