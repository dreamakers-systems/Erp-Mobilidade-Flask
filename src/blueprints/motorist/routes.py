# pylint: disable=no-value-for-parameter
"""Motorist Routes"""


from flask import Blueprint, redirect, render_template, request, url_for

from src.database.querys import MotoristsQuerys, RunsQuerys

from .src.uploads import MotoristsDataParsing

motorist_app = Blueprint('motorist_app', __name__, url_prefix='/motorists/')


@motorist_app.route('/', methods=['GET'])
def get_motorits():
    """Get all motorists in database"""
    motorists = MotoristsQuerys.show()
    return render_template('pages/motorists/show.html', motorists=motorists)


@motorist_app.route('/create', methods=['POST', 'GET'])
def create():
    """Create a new motorist"""
    if request.method == 'POST':
        name = request.form.get('name')
        data_json = {'comission': 'default'}
        MotoristsQuerys.create_motorist(name, data_json)
        RunsQuerys.create_table(name)
        return redirect(url_for('motorist_app.create'))

    return render_template('pages/motorists/create.html')


@motorist_app.route('/delete/<motorist_id>:int', methods=['POST'])
def delete(motorist_id: int):
    """Delete a motorist"""
    print(MotoristsQuerys.delete(motorist_id))
    return redirect(url_for('motorist_app.show'))


@motorist_app.route('/uploads', methods=['POST', 'GET'])
def uploads():
    """upload datas"""
    if request.method == 'POST':
        archives = request.files.getlist('image[]')
        MotoristsDataParsing(archives)

        return redirect(url_for('motorist_app.uploads'))
    return render_template('pages/motorists/uploads.html')


@motorist_app.route('/edit/<motorist_id>', methods=['POST', 'GET'])
def edit(motorist_id):
    """Create a new motorist"""
    if request.method == 'POST':
        name = request.form.get('name')
        data_json = {'comission': 'default'}
        MotoristsQuerys.create_motorist(name, data_json)
        RunsQuerys.create_table(name)
        return redirect(url_for('motorist_app.create'))

    motorist = MotoristsQuerys.get_id(motorist_id)

    return render_template('pages/motorists/edit.html', motorist=motorist)

@motorist_app.route('/revenues/show/<motorist_id>', methods=['POST', 'GET'])
def revenues(motorist_id):
    """Create a new motorist"""
    if request.method == 'POST':
        name = request.form.get('name')
        data_json = {'comission': 'default'}
        MotoristsQuerys.create_motorist(name, data_json)
        RunsQuerys.create_table(name)
        return redirect(url_for('motorist_app.create'))

    motorist = MotoristsQuerys.get_id(motorist_id)

    return render_template('pages/motorists/edit.html', motorist=motorist)