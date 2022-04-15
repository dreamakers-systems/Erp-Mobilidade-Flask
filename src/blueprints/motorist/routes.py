""" Motorist Routes """

import logging

from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from flask_cors import CORS

from src.database.querys import MotoristsQuerys
from src.database.json_schemas import MotoristJsonSchema
from src. database.querys import RunsQuerys

from .uploads import MotoristsDataParsing

motorist_app = Blueprint(
    "motorist_app", __name__,
    url_prefix="/motorists/")

logging.getLogger('flask_cors').level = logging.DEBUG
CORS(motorist_app,)


@motorist_app.route("/", methods=["GET"])
def get_motorits():
    "Get all motorists in database"
    motorists = MotoristsQuerys.check_motorists()
    return render_template("pages/motorists/show.html", motorists=motorists)


@motorist_app.route("/create", methods=["POST", "GET"])
def create():
    "Create a new motorist"
    if request.method == "POST":
        name = request.form.get("name")
        data_json = {"comission": "defout"}
        MotoristsQuerys.create_motorist(name, data_json)
        RunsQuerys.create_table(name)
        return redirect(url_for("motorist_app.create"))

    return render_template("pages/motorists/create.html")


@motorist_app.route("/delete", methods=["POST"])
def delete_motorist():
    """ Delete a motorist """
    motorist_id = request.json.get("id")
    print((motorist_id))
    MotoristsQuerys.delete_motorist(motorist_id)
    schema = MotoristJsonSchema()

    motorists = {
        "motorists":[
            schema.dump(i) for i in MotoristsQuerys.check_motorists()]}
    return jsonify(motorists)


@motorist_app.route("/uploads", methods=["POST", "GET"])
def uploads():
    """ upload datas """
    if request.method == "POST":
        archives = request.files.getlist("image[]")
        MotoristsDataParsing(archives)

        return redirect(url_for("motorist_app.uploads"))
    return render_template("pages/motorists/uploads.html")


@motorist_app.route("/settings", methods=["POST", "GET"])
def settings():
    """ upload datas """
    if request.method == "POST":
        return redirect(url_for("motorist_app.settings"))
    return render_template("pages/motorists/settings.html")
