# pylint: disable=import-outside-toplevel
""" Aplication Factory """

from flask import Flask


def init_app():
    " Factory method for create the Flask App "
    app = Flask(__name__)

    from .settings import Config
    app.config.from_object(Config)

    with app.app_context():
        return app
