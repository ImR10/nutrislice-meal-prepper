from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    pass

@auth.route('/login', methods=['POST'])
def login():
    pass