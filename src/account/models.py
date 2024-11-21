from flask_login import UserMixin
import json
import os


class User(UserMixin):
    def __init__(self, username, password):
        self.id = username
        self.password = password

    @staticmethod
    def load_users():
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        file_path = os.path.join(project_root, "lib", "users.json")
        with open(file_path) as f:
            return json.load(f)

    @staticmethod
    def get_user(username):
        users = User.load_users()
        for user in users:
            if user['username'] == username:
                return User(username=user['username'], password=user['password'])
        return None
