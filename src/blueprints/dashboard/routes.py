
""" Rotas de Dashboard """

from flask import Blueprint, render_template

dashboard_app = Blueprint(
    "dashboard", __name__,
    url_prefix="/")


@dashboard_app.route('/', methods=['GET'])
def dashboard():
    """ Exibe a pagina principal da aplicação """
    return render_template("pages/dashboard/index.html")
