# pylint: disable = consider-using-f-string
from datetime import datetime
from time import strftime, strptime
from typing import List

from src.database import RunsBase
from src.database.db_connection import db_connector
from src.database.models import runs_factory


class RunsQuerys:
    """A Consult if name alredy exits"""

    @classmethod
    @db_connector
    def create_table(cls, connection, name):
        """someting"""

        runs_factory(name)
        engine = connection.get_engine()
        RunsBase.metadata.create_all(engine)

    @classmethod
    @db_connector
    def insert(cls, connection, name, data):
        """someting"""

        for item in data:
            connection.session.execute(
                'INSERT OR IGNORE INTO {}'
                '(date_time, valor, operation)'
                "VALUES ('{}','{}','{}')".format(
                    f'RUNS_{name}', item[0], item[1], item[2]
                )
            )
        connection.session.commit()

    @classmethod
    @db_connector
    def search_daterange(cls, connection, name: str, date_range: List) -> List:
        """ex:
        '2021-01-15 07:42:00', '2021-01-20 16:20:00'"""

        mot = runs_factory(name)
        runs = (
            connection.session.query(mot)
            .filter(mot.date_time.between(*date_range))
            .all()
        )
        _runs = list(
            map(lambda run: (
                run.date_time.strftime('%d/%m/%Y'),
                run.valor,
                run.operation), runs))
        return _runs

        # "SELECT DATE_FORMAT(date_time, '%d-%m-%Y %H:%i'), valor, operator\
        # FROM base_g4.{}\
        # WHERE date_time\
        # BETWEEN '{}' AND '{}';".format(name, date_range[0], date_range[1]))

        # list_ = [[tables[0], tables[1], tables[2]]
        #     for tables in connect.cursor.fetchall()]
