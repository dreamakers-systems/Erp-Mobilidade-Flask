from src.database.db_connection import DBConnectionHendler
from src.database.models import RevenuesPorcents


class RevenuesQuery:
    @classmethod
    def create_motorist_group(
        cls, name, porcent_one, porcent_two, porcent_tree
    ):
        """someting"""
        with DBConnectionHendler() as db_connection:
            try:
                new_rule = RevenuesPorcents(
                    name=name,
                    porcent_one=porcent_one,
                    porcent_two=porcent_two,
                    porcent_tree=porcent_tree,
                )

                db_connection.session.add(new_rule)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def all(cls):
        """someting"""
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(RevenuesPorcents).all()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def update_porcent(cls):
        """someting"""
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(RevenuesPorcents).all()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def find(cls, porcent_id):
        """someting"""
        with DBConnectionHendler() as db_connection:
            try:
                return (
                    db_connection.session.query(RevenuesPorcents)
                    .filter_by(id=porcent_id)
                    .first()
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
