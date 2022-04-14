# pylint: disable: too-few-public-methods
# pylint: disable=consider-using-f-string
""" User Querys"""

from src.database.db_connection import DBConnectionHendler
from src.database.models.motorist import Motorists
from sqlalchemy import inspect

class MotoristsQuerys:
    """ A Consult if name alredy exits """
    @classmethod
    def check_name(cls, name):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(Motorists).filter_by(name=name).first()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def check_motorists(cls):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                motorists = list(inspect(db_connection.get_engine()).get_table_names())
                motorists.pop(-1)
                return motorists
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def create_motorist(cls, name, data_json):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                new_user = Motorists(name=name, data_json=data_json)
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()


    @classmethod
    def get_id(cls, name):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(Motorists).filter_by(name=name).first()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()


    @classmethod
    def delete_motorist(cls, motorist_id):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                motorist = db_connection.session.query(Motorists).filter_by(id=motorist_id).first()
                db_connection.session.delete(motorist)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def create_motorists_runs(cls, name):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                db_connection.session.execute(
                    "CREATE TABLE IF NOT EXISTS {}(" \
                    "date_time DATETIME UNIQUE, " \
                    "valor INTEGER(11) NOT NULl, " \
                    "operator VARCHAR(1));".format(name.replace(" ", "_")))
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()


    @classmethod
    def insert(cls, name, data):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                for item in data:
                    db_connection.session.execute(
                    "INSERT OR IGNORE INTO {}" \
                    "(date_time, valor, operator)" \
                    "VALUES ('{}','{}','{}')".format(
                    name, item[0], item[1], item[2]))
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def get(cls):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                db = inspect(db_connection.get_engine())
                print(db.get_table_names())
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()