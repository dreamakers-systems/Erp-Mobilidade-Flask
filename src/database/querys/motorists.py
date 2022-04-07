# pylint: disable: too-few-public-methods

""" User Querys"""

from src.database.db_connection import DBConnectionHendler
from src.database.models.motorist import Motorists

class CheckName:
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


class CheckMotorists:
    """ A Consult if name alredy exits """
    @classmethod
    def check_motorists(cls):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(Motorists).all()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

class CreateMotorists:
    """ Create a new user """
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


class GetId:
    """ A Consult if name alredy exits """
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


class DeleteMotorist:
    """ Delete a motorist """
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

class CreteRunsTable:
    """ Insert mmany motorists """
    @classmethod
    def delete_motorist(cls, motorist_id):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                # motorist = db_connection.session.
                # db_connection.session.delete(motorist)
                # db_connection.session.commit()
                pass
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
