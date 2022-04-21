from typing import List
from src.database import DBConnectionHendler
from src.database.models import Client


class ClientQuerys:
    """ Criando um novo cliente """
    @classmethod
    def new(cls, nome):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                client = Client(name=nome.upper())
                
                db_connection.session.add(client)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()


    @classmethod
    def get_all(cls) -> List:
        """ Retorna uma lista de todos os clients """
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(Client).all()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()



    @classmethod
    def get_id(cls, client_id):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(Client).filter_by(id=client_id).first()
        
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()


    """ Create a new user """
    @classmethod
    def delete(cls, client_id):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                client = db_connection.session.query(Client).filter_by(id=client_id).first()
                db_connection.session.delete(client)
                db_connection.session.commit()

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
