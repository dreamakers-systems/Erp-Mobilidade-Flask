# pylint: disable= no-value-for-parameter
"""Resolving request to export invoices"""

import os
import tarfile
from datetime import datetime
from glob import glob
from tempfile import TemporaryDirectory
from typing import List, Tuple

from flask import send_file

from src.blueprints.revenues.src import report
from src.blueprints.revenues.src.load import DataExtructure
from src.database.models.revenues import RevenuesPorcents
from src.database.querys.drivers import MotoristsQuerys
from src.database.querys.revenues import RevenuesQuery
from src.database.querys.runs import RunsQuerys


class Invoices:
    """Manage invoice cals."""

    def __init__(self, daterange, option: Tuple) -> None:
        """sumary_line

        Keyword arguments:
        datetime -- Is a daterange
        option -- especify a driver or all
        Return: Return a tar object to send with a response.
        """

        self.option = option
        self.daterange = daterange
        self.media_path = os.path.abspath('./media')

    def match_options(self):
        """Match method to execute correct code."""
        match self.option:
            case 'TODOS':
                return self.get_all_invoices()
            case _:
                invoice = self.get_invoice(self.option)
                resp = send_file(
                    invoice,
                    mimetype='png',
                    as_attachment=True,
                    attachment_filename=os.path.join(self.media_path, f'{self.option}.png'))
                return resp


    def save_files(self, drivers):
        with TemporaryDirectory() as tmpdir:
            tar_path = os.path.join(tmpdir, 'result.tar')
            
            with tarfile.open(name=tar_path, mode='w:gz') as tar_file:
                
                for driver in drivers:
                    self.get_invoice(driver).save(os.path.join(
                        tmpdir, driver + '.png'))

                for item in os.listdir(tmpdir):
                    tar_file.add(
                        os.path.join(tmpdir, item),  arcname=f'{item}')
                    
            resp = send_file(
                tar_path,
                mimetype='application/x-tar',
                as_attachment=False,
                attachment_filename=f'Fechamento - {self.daterange}.tar',)
            
            return resp
            
    def get_all_invoices(self):
        "Get invoices from all motorists."
        drivers = list(
            map(lambda driver: driver.name, MotoristsQuerys.show()))

        drivers.__delitem__(-1)
        

        for item in glob(f'{self.media_path}/*'):
            os.remove(item)

        return self.save_files(drivers)

    def get_invoice(self, name: str):
        "Get invoice of a driver"
        runs: List = RunsQuerys.search_daterange(
            name, self.daterange)

        group = MotoristsQuerys.get_group(name)

        porcent: RevenuesPorcents = RevenuesQuery().get_by_name(group)

        data_porcent = {
            "10":(porcent.porcent_one, -100 + porcent.porcent_one),
            "12":(porcent.porcent_two, -100 + porcent.porcent_two),
            "23":(porcent.porcent_tree, -100 + porcent.porcent_tree)
        }

        analyse = DataExtructure(runs, data_porcent).get_result()

        report_revenues = report.save_report(
            name,
            datetime.strptime(self.daterange[0][:-9], '%Y-%m-%d').strftime('%d/%m/%Y'),
            datetime.strptime(self.daterange[1][:-9], '%Y-%m-%d').strftime('%d/%m/%Y'),
            analyse)

        return report_revenues

    def get_result(self):
        """Return result."""
        return self.match_options()
