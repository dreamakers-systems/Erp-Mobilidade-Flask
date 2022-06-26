# pylint: disable = consider-using-f-string
from typing import List

from src.database import RunsBase
from src.database.db_connection import db_connector
from src.database.models import runs_factory


class RunsQuerys:
    """A Consult if name alredy exits"""

    @classmethod
    @db_connector
    def create_table(cls, connection, name):
        """Create runs table."""

        runs_factory(name)
        engine = connection.get_engine()
        RunsBase.metadata.create_all(engine)

    @classmethod
    @db_connector
    def insert(cls, connection, name, data):
        """Insert runs in database."""

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
        """Search all runs in a range:

        name -- driver name
        date_range -- is a list with two datetimes.

        For exemple:
                '2021-01-15 07:42:00', '2021-01-20 16:20:00'

        Return a list with all runs
        """

        mot = runs_factory(name)
        runs = (
            connection.session.query(mot)
            .filter(mot.date_time.between(*date_range))
            .all()
        )

        _runs = list(
            map(
                lambda run: (
                    run.date_time.strftime('%d/%m/%Y'),
                    run.valor,
                    run.operation,
                ),
                runs,
            )
        )
        return _runs
