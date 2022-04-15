""" Motorist Routes """

import logging

from flask import Blueprint, render_template


clients_app = Blueprint("clients_app", __name__, url_prefix="/clients/")


@clients_app.route("/", methods=["GET"])
def get_motorits():
    "Get all motorists in database"
    return render_template("pages/clientes.html")
