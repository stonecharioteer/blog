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
base_oso.load_str("""allow(user: User, "can", "logout");""")
base_oso.load_str("""allow(user: User, "can", "logout") if user.id = "admin";""")

oso_extension = FlaskOso(oso=base_oso)
oso_extension.init_app(app)
oso_extension.require_authorization(app)


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
    oso_extension.authorize(actor=current_user, action="can_get", resource="secure_route")
    return jsonify(msg="this is a login-only route accessible only by admin")


@app.route("/logout")
@login_required
def logout():
    oso_extension.authorize(actor=current_user, action="can", resource="logout")
    # this line will allow all logged in users to be a ble to logout.  logout_user()
    logout_user()
    return jsonify(msg="you have been logged out")
