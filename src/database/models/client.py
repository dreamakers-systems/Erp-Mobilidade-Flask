""" Models for Clients"""


from sqlalchemy import String, Column, Integer, JSON

from src.database import Base


class Client(Base):
    """Clients Table"""

    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)
    data_json = Column(JSON)

    def __rep__(self):
        """True, as all users are active."""
        return f"Usr [name={self.name}]"
