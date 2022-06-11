from src.database.db_connection import db_connector
from src.database.models import RevenuesPorcents


class RevenuesQuery:
    @classmethod
    @db_connector
    def create_motorist_group(
        cls, connection, name, porcent_one, porcent_two, porcent_tree
    ):
        """someting"""
        new_rule = RevenuesPorcents(
            name=name,
            porcent_one=porcent_one,
            porcent_two=porcent_two,
            porcent_tree=porcent_tree,
        )

        connection.session.add(new_rule)
        connection.session.commit()

    @classmethod
    @db_connector
    def all(cls, connection):
        """someting"""
        return connection.session.query(RevenuesPorcents).all()

    @classmethod
    @db_connector
    def update_porcent(cls, connection, porcent_one, porcent_two, porcent_tree):
        """someting"""
        return connection.session.query(RevenuesPorcents).all()

    @classmethod
    @db_connector
    def get_by_name(cls, connection, name):
        """someting"""
        return (
            connection.session.query(RevenuesPorcents)
            .filter_by(name=name)
            .first()
        )
