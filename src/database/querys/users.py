"""User Querys"""

from typing import List

from src.database.db_connection import db_connector
from src.database.models import User


class UserQuerys:
    """querys from users"""

    @classmethod
    @db_connector
    def get_by_id(cls, connection, user_id):
        """Get a User by id."""
        return connection.session.query(User).filter_by(id=int(user_id))

    @classmethod
    @db_connector
    def get_by_email(cls, connection, email) -> List:
        """Select a user by email"""
        return connection.session.query(User).filter_by(email=email).first()

    @classmethod
    @db_connector
    def create(cls, connection, name, email, password) -> User:
        """Create_user"""
        user = User(
            name=name,
            email=email,
        )
        user.set_password(password)
        connection.session.add(user)
        connection.session.commit()  # Create new user
        return user
