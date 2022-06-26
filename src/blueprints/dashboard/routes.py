# pylint: disable=no-value-for-parameter,unused-variable
"""Rotas de Dashboard"""

from flask import Blueprint, render_template

from src.database.querys import ClientQuerys, MotoristsQuerys

dashboard_app = Blueprint('dashboard', __name__, url_prefix='/')


@dashboard_app.route('/', methods=['GET'])
def dashboard():
    """Main dashboard of application."""
    motorist_num = len(MotoristsQuerys.show())
    client_num = len(ClientQuerys.get_all())
    runs = None
    schedule = None
    weekly_runs = None

    return render_template(
        'pages/dashboard/index.html',
        motorist_num=motorist_num,
        client_num=client_num,
    )
