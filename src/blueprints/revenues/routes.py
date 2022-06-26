# pylint: disable=no-value-for-parameter
"""Motorist Routes"""


import datetime
import re

from flask import (Blueprint, redirect, render_template, request,
                   url_for)

from src.blueprints.revenues.src.invoices import Invoices
from src.database.querys import MotoristsQuerys, RevenuesQuery

revenues_app = Blueprint('revenues_app', __name__, url_prefix='/revenues/')


@revenues_app.route('/settings', methods=['GET'])
def show():
    """Get all porcent groups in database"""
    porcents = RevenuesQuery.get_all()
    return render_template('pages/revenues/show.html', porcents=porcents)


@revenues_app.route('/create', methods=['POST', 'GET'])
def create():
    """Create a new settings rule in database."""
    if request.method == 'POST':
        group_name = request.form.get('group_name')
        porcent_one = request.form.get('porcent_one')
        porcent_two = request.form.get('porcent_two')
        porcent_tree = request.form.get('porcent_tree')
        RevenuesQuery.create_motorist_group(
            group_name, porcent_one, porcent_two, porcent_tree
        )

        return redirect(url_for('revenues_app.show'))

    return render_template('pages/revenues/create.html')


@revenues_app.route('/edit/<porcent_id>', methods=['POST', 'GET'])
def edit(porcent_id):
    """Edit rules of a porcent groups"""
    if request.method == 'POST':

        porcent_one = request.form.get('porcent_one')
        porcent_two = request.form.get('porcent_two')
        porcent_tree = request.form.get('porcent_tree')

        RevenuesQuery.update_porcent(porcent_one, porcent_two, porcent_tree)

        return redirect(url_for('revenues_app.show'))

    porcent = RevenuesQuery.get_by_name(porcent_id)
    print(porcent)
    return render_template('pages/revenues/edit.html', porcent=porcent)


@revenues_app.route('/invoices', methods=['POST', 'GET'])
def invoices():
    """Export  invoice from motorists"""

    motorists = list(map(lambda driver: driver.name, MotoristsQuerys.show()))

    motorists.__delitem__(-1)

    if request.method == 'POST':

        option = request.form.get('option')
        datetime_range = request.form.get('daterange')

        date_one = datetime_range[:10]
        date_two = datetime_range[11:-1]
        date_two = re.findall(r'\d+/\d+/\d+', date_two)[0]

        date_time_one = datetime.datetime.strptime(
            date_one, '%m/%d/%Y'
        ).strftime('%Y-%m-%d %H:%M:%S')

        date_time_two = datetime.datetime.strptime(
            date_two, '%m/%d/%Y'
        ).strftime('%Y-%m-%d %H:%M:%S')

        resp = Invoices((date_time_one, date_time_two), option).get_result()

        return resp

    motorists.insert(0, 'TODOS')
    return render_template('pages/revenues/invoices.html', motorists=motorists)
