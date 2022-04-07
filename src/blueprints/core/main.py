""" Auth Server """

import os

from flask import Blueprint, jsonify, current_app, request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager

auth = Blueprint("auth", __name__)

# Setup the Flask-JWT-Extended extension
current_app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_KEY")
jwt = JWTManager(current_app)

@auth.route("/token", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return jsonify({"msg": "Bad email or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)