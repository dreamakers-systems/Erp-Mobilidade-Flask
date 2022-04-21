""" Clientes """

from flask import Blueprint, render_template


clients_app = Blueprint("clients_app", __name__, url_prefix="/clients/")


@clients_app.route("/", methods=["GET"])
def show():
    """Exibe a pagina de clientes
    """
    
    return render_template("pages/clientes.html")
