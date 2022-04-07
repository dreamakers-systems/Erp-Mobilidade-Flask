""" Motorist Routes """


from flask import Blueprint, render_template
from flask_cors import CORS


revenues_app = Blueprint(
    "revenues_app", __name__,
    url_prefix="/revenues/")

# logging.getLogger('flask_cors').level = logging.DEBUG
CORS(
    revenues_app,
    )


@revenues_app.route("/", methods=["GET"])
def get_motorits():
    "Get all motorists in database"
    return render_template("pages/revenues.html")
