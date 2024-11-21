from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from flask_login import LoginManager
from src.account.models import User

load_dotenv()

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'default-secret-key'
    app.config['SESSION_COOKIE_SAMESITE'] = 'None'
    CORS(app, supports_credentials=True)

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User(user_id) if user_id else None

    from src.account.routes import account_bp
    app.register_blueprint(account_bp)

    return app
