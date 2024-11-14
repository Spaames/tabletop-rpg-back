from flask import Blueprint, jsonify, request
import json
import os

account_bp = Blueprint('account', __name__)

def load_users():
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    file_path = os.path.join(project_root, 'lib', 'users.json')

    with open(file_path) as f:
        return json.load(f)


@account_bp.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    users = load_users()

    for user in users:
        if user['username'] == username and user['password'] == password:
            return jsonify({"status": "success", "message": "Login successful"}), 200
    return jsonify({"status": "failed", "message": "Invalid credentials"}), 401



