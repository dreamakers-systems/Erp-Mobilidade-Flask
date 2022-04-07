""" Models for Motorists"""

from typing import Dict

from sqlalchemy import String, Column, Integer, JSON

from src.database import Base


class Motorists(Base):
    """ Motorist Table """
    __tablename__ = 'motorists'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)
    data_json = Column(JSON)

    def __init__(self, name: str, data_json: Dict) -> None:
        """ Interface """
        self.name = name
        self.data_json = data_json


    def __rep__(self):
        """True, as all users are active."""
        return f"Usr [name={self.name}]"
