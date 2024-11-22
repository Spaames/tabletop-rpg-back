from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

from src.account.models import User

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'default-secret-key'

    CORS(app)

    from src.account.routes import account_bp
    app.register_blueprint(account_bp)

    return app
