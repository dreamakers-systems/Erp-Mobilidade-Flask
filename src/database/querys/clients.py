from typing import List

from src.database import DBConnectionHendler
from src.database.db_connection import db_connector
from src.database.models import Client


class ClientQuerys:
    """Criando um novo cliente"""

    @classmethod
    @db_connector
    def new(cls, connection, name):
        """someting"""
        client = Client(name=name.upper())
        connection.session.add(client)
        connection.session.commit()

    @classmethod
    @db_connector
    def get_all(cls, connection) -> List:
        """Retorna uma lista de todos os clients"""
        return connection.session.query(Client).all()

    @classmethod
    @db_connector
    def get_id(cls, connection, client_id):
        """Select by id"""
        return connection.session.query(Client).filter_by(id=client_id).first()

    @classmethod
    @db_connector
    def delete(cls, connection, client_id: int) -> None:
        client = (
            connection.session.query(Client).filter_by(id=client_id).first()
        )
        connection.session.delete(client)
        connection.session.commit()
