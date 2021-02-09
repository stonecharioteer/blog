from flask import Flask, request, jsonify
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from oso import Oso
from flask_oso import FlaskOso, skip_authorization

app = Flask(__name__)
app.config["SECRET_KEY"] = "this shouldn't go into the code. store it in a config."
login_manager = LoginManager()
login_manager.init_app(app)


class User:
    def __init__(self, id=None):
        self.id = id

    @staticmethod
    def get(id):
        if isinstance(id, str):
            return User(id)
        else:
            return None

    def is_authenticated(self):
        return self.id is not None

    def is_active(self):
        return self.id is not None

    def is_anonymous(self):
        return self.id is None

    def get_id(self):
        return self.id


base_oso = Oso()
base_oso.register_class(User)
base_oso.load_file("policies.polar")
flask_oso_plugin = FlaskOso(oso=base_oso)
flask_oso_plugin.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/login", methods=["POST"])
@skip_authorization # authorization should be skipped for a login route.
def login():
    username = request.json.get("username")
    # no password check
    user = User(username)
    login_user(user, remember=True)
    return jsonify(msg="login was a success!")


@app.route("/secure_route")
@login_required
def secure_route():
    username = current_user.id
    if flask_oso_plugin.oso.is_allowed(User(username), "can_access","secure_route"):
        return jsonify(msg="this is a login-only route accessible only by admin")
    else:
        return "access denied", 403


@app.route("/logout")
@login_required
def logout():
    username = current_user.id
    if flask_oso_plugin.oso.is_allowed(User(username), "can", "logout"):
    # this line will allow all logged in users to be a ble to logout.  logout_user()
        logout_user()

        return jsonify(msg="you have been logged out")
    else:
        return "access denied", 403
