from flask import Flask
import oso
from flask_oso import FlaskOso, skip_authorization

app = Flask(__name__)
base_oso = oso.Oso()
oso_extension = FlaskOso(oso=base_oso)
base_oso.load_str("""allow("anyone","can_visit","index");""")
oso_extension.init_app(app)


@app.route("/")
def index_route():
    oso_extension.authorize(actor="anyone", action="can_visit", resource="index")
    return "hello world"


@app.route("/unvisitable")
def unpermissable_route():
    oso_extension.authorize(actor="noone", action="can_visit", resource="this route")


@app.route("/hello")
@skip_authorization
def hello_route():
    return "hello again"


oso_extension.require_authorization(app)
