from flask import Flask, request, jsonify
from flask_login import LoginManager, login_required, login_user, logout_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


class User:
    def __init__(self, id=None):
        self.id = id

    @staticmethod
    def get(id):
        if id == "admin":
            return User("admin")
        else:
            return None

    def is_authenticated(self):
        return self.id == "admin"

    def is_active(self):
        return self.id == "admin"

    def is_anonymous(self):
        return self.id is None

    def get_id(self):
        return self.id


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/login", methods=["POST"])
def login():
    username = request.get("username")
    password = request.get("password")

    if username == "admin" and password == "admin":
        user = User("admin")
        login_user(user)
        return jsonify(msg="login was a success!")


@app.route("/secure_route")
@login_required
def secure_route():
    return jsonify(msg="this is a login-only route")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return jsonify(msg="you have been logged out")
