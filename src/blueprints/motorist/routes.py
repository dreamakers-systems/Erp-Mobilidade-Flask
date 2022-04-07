""" Motorist Routes """

import logging

from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from flask_cors import CORS

from src.database.querys import CreateMotorists, CheckMotorists, CheckName, DeleteMotorist
from src.database.json_schemas import MotoristJsonSchema

motorist_app = Blueprint(
    "motorist_app", __name__,
    url_prefix="/motorists/")

logging.getLogger('flask_cors').level = logging.DEBUG
CORS(
    motorist_app,
    )




@motorist_app.route("/", methods=["GET"])
def get_motorits():
    "Get all motorists in database"
    motorists = CheckMotorists.check_motorists()
    return render_template("pages/motorists/motorists.html", motorists=motorists)

@motorist_app.route("/create", methods=["POST", "GET"])
def new_motorits():
    "Create a new motorist"
    if request.method == "POST":
        name = request.form.get("name")
        data_json = {"comission": "defaut"}
        CreateMotorists.create_motorist(name, data_json)
        return redirect(url_for("motorist_app.get_motorits"))

    return render_template("pages/motorists/create.html")

@motorist_app.route("/delete", methods=["POST"])
def delete_motorist():
    """ Delete a motorist """
    motorist_id = request.json.get("id")
    print((motorist_id))
    DeleteMotorist.delete_motorist(motorist_id)
    schema = MotoristJsonSchema()

    motorists = {
        "motorists":[
            schema.dump(i) for i in CheckMotorists.check_motorists()]}
    return jsonify(motorists)

