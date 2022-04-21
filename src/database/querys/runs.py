# pylint: disable = consider-using-f-string
from typing import List
from datetime import date, datetime

from sqlalchemy import Table

from src.database import RunsBase
from src.database.db_connection import DBConnectionHendler
from src.database.models import RunsFactory


class RunsQuerys:
    """A Consult if name alredy exits"""

    @classmethod
    def create_table(cls, name):
        """someting"""
        with DBConnectionHendler() as db_connection:
            try:

                RunsFactory(name)
                engine = db_connection.get_engine()
                RunsBase.metadata.create_all(engine)
            except:
                db_connection.session.rollback()
                ...
            finally:
                db_connection.session.close()

    @classmethod
    def insert(cls, name, data):
        """someting"""
        with DBConnectionHendler() as db_connection:
            try:
                for item in data:
                    db_connection.session.execute(
                        "INSERT OR IGNORE INTO {}"
                        "(date_time, valor, operation)"
                        "VALUES ('{}','{}','{}')".format(
                            f"RUNS_{name}", item[0], item[1], item[2]
                        )
                    )
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def search_daterange(cls, name: str, date_range: List):
        """someting"""
        with DBConnectionHendler() as db_connection:
            try:
                data_1 =  datetime(2021, 1, 12)
                query = db_connection.session
                print(query)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

