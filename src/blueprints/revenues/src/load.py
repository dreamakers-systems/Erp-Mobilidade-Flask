"""Load informations to analysis"""

import locale
import os
from typing import Dict, List

import pandas as pd
from pandas import DataFrame

from .analyse import DataAnalyse

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


class DataExtructure(DataAnalyse):
    """object to load, analyse and export data"""

    def __init__(self, data_list: List, porcents: Dict) -> None:
        """Receave data from a sql search
        :data_frame = [[dd-mm-yy, int, (- or +)], ...]

        The class receave tree parameters in a json to
        calculate all rown in the dataframe
        :dict_ = {
            "10":(10, -90),
            "12":(12, -85),
            "23":(23, -80)
        }"""

        self.data_list = data_list
        self.porcents = porcents

    def get_data_frame(self) -> DataFrame:
        """set a data with faturation"""
        collumns = ['Valor', 'Quantidade', 'Recebido', 'A Pagar']
        data = self.analyse_faturation()
        df_data = pd.DataFrame(data, columns=collumns, index=None)
        df_data['Valor'] = df_data['Valor'].map(locale.currency)
        df_data['Recebido'] = df_data['Recebido'].map(locale.currency)
        df_data['A Pagar'] = df_data['A Pagar'].map(locale.currency)
        return df_data

    def get_result(self) -> List:
        """Get result is used returt final format."""
        return self.get_data_frame().values.tolist()

    def get_faturation(self):
        """Get Result Faturation"""
        return self.analyse_faturation()

    def save_csv(self, directory, name):
        """Save in csv"""
        self.get_data_frame().to_csv(
            os.path.join(directory, name + '.csv'),
            header=True,
            encoding='utf-8',
            index=False,
        )
