# pylint: disable=no-value-for-parameter
"""Clientes"""


import os

from flask import Blueprint, redirect, render_template, request, url_for

from src.database.querys.clients import ClientQuerys

clients_app = Blueprint('clients_app', __name__, url_prefix='/clients/')


@clients_app.route('/', methods=['GET'])
def show():
    """Show client main page."""
    clients = ClientQuerys.get_all()
    return render_template('pages/clients/show.html', clients=clients)


@clients_app.route('/novo', methods=['GET', 'POST'])
def new():
    """sumary_line"""
    if request.method == 'POST':
        name = request.form['name']
        print(name)

        ClientQuerys.new(name.upper())
        return redirect(url_for('clients_app.show'))
    return render_template('pages/clients/new.html')


@clients_app.route('/editar/<int:id_cliente>', methods=['GET', 'POST'])
def edit(id_cliente):
    """Edit Client infos."""
    cliente = ClientQuerys.get_id(id_cliente)
    image = os.path.join('/media/equipamentos/', cliente.nome + '.jpeg')
    return render_template(
        '/pages/cliente/edit.html', cliente=cliente, image=image
    )


@clients_app.route('/delete/<int:id_cliente>', methods=['GET', 'POST'])
def delete(id_cliente: int):
    """Delete a cliente."""
    ClientQuerys.delete(id_cliente)
    return redirect(url_for('clients_app.show'))
