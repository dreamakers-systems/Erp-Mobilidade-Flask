
""" Rotas de Dashboard """

from flask import Blueprint, render_template

from src.database.querys import MotoristsQuerys, ClientQuerys

dashboard_app = Blueprint(
    "dashboard", __name__,
    url_prefix="/")


@dashboard_app.route('/', methods=['GET'])
def dashboard():
    motorist_num = len(MotoristsQuerys.show())
    client_num = len(ClientQuerys.get_all())
    runs = None
    schedule = None
    weekly_runs = None
    
    """ Exibe a pagina principal da aplicação """
    return render_template("pages/dashboard/index.html",
                           motorist_num=motorist_num,
                           client_num=client_num)

