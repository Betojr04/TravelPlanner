from flask import Blueprint, render_template

trip_routes = Blueprint("trip_routes", __name__)


@trip_routes.route("/")
def home():
    return render_template("index.html")
