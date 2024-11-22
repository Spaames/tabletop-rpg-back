from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from src.account.models import User

account_bp = Blueprint('account', __name__)


@account_bp.route('/api/login', methods=['POST'])
@cross_origin(origins='http://localhost:3000')
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.get_user(username)

    if user and user.password == password:
        return (jsonify({
            "status": "success",
            "username": username,
            "message": "Login successful"}),
            200)
    else:
        return jsonify({"status": "failed", "message": "Invalid credentials"}), 401