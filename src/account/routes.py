from flask import Blueprint, jsonify, request, session
from flask_login import login_user, logout_user, current_user, login_required
from src.account.models import User

account_bp = Blueprint('account', __name__)


@account_bp.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.get_user(username)

    if user and user.password == password:
        login_user(user)
        return jsonify({"status": "success", "username": username, "message": "Login successful"}), 200
    else:
        return jsonify({"status": "failed", "message": "Invalid credentials"}), 401


@account_bp.route('/api/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"status": "success", "message": "Logged out successfully"}), 200

