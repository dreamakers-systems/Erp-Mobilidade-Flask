""" Receave mmotorist runs """

import datetime
import re

from werkzeug.datastructures import FileStorage

from src.database.querys import MotoristsQuerys
from src.database.querys import RunsQuerys

class MotoristsDataParsing:
    """Recebe uma requisição e constroi os
    objetos dos motoristas e armazena em um dicionario
    """
    def __init__(self, request_files) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.request_files = request_files
        self.set_motorists()

    def set_motorists(self):
        """ Set name for the motorist """
        for motorist in self.request_files:
            data = ParsedMotoristData(motorist).get()
            name = motorist.filename[:-4][29:].replace(" ", "_")
            data_json = {"comission": "defout"}
            MotoristsQuerys.create_motorist(name, data_json)
            RunsQuerys.create_table(name)
            RunsQuerys.insert(name, data)



class ParsedMotoristData:
    """Percore toda a conversa pegando apenas
    as linhas correspondentes aos codigos usados em
    nossa regra de negocio
    """
    def __init__(self, talk: FileStorage):
        """Recebe uma conversa
        """
        self.data_frame = []
        self.filter_talk(talk, "G4 MOBILE", "reais")

    def get(self):
        """ Metodo para acessar o dataframe"""
        return self.data_frame

    def get_datetime(self, line: str) -> str:
        """ Realiza o parsing da data """
        date = re.findall(r"\d+/\d+/\d+", line)
        date = datetime.datetime.strptime(date[0], "%d/%m/%Y").strftime("%Y-%m-%d")
        if not date:
            date = self.data_frame[-1][0]
        hour = re.findall(r"\d+\:\d+", line)
        hour = hour[0]+':00'

        try:
            if date_time == self.data_frame[-1][0]:
                correction = str(int(date_time[14:-3]) + 1)
                date_time_list = list(date_time)
                date_time_list[14] = correction[0]
                date_time_list[15] = correction[1]
                date_time = "".join(date_time_list)
                print(date_time, self.data_frame[-1])
        except Exception as error:
            print(error)
        return f"{date} {hour}"

    def get_valor(self, line: str) -> str:
        """Realiza o parsing do valor"""
        return re.findall(r"\d+\s+reais", line)[0][:-6]

    def get_operation(self, line: str) -> str:
        """Realiza o parsing do valor"""
        if 'desconto no boleto' in line:
            operation = '-'
        else:
            operation = '+'
        return operation

    def filter_talk(self, talk, name, rule):
        """Percorre toda a conversa: talk
        procurando por
            Refatora as Linhas no formato
            datetime | valor | operation
        """
        for line in talk:
            line = line.decode("utf-8")
            if name and rule in line: #pylint: disable=simplifiable-condition
                try:
                    format_line = [
                        self.get_datetime(line),
                        self.get_valor(line),
                        self.get_operation(line)]
                    self.data_frame.append(format_line)
                except Exception as error:
                    print(error, line)
                    return True


