""" co Server """

import os

from flask import Blueprint, render_template

core_app = Blueprint("core_app", __name__,
                     url_prefix="/core")

@core_app.route('/', methods=['GET'])
def method_name():
    return render_template("")
