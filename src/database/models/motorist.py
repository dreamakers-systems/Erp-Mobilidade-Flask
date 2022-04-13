""" Models for Motorists"""

from typing import Dict

from sqlalchemy import String, Column, Integer, JSON, DateTime
from sqlalchemy.orm import relationship

from src.database import Base

class Motorists(Base):
    """ Motorist Table """
    __tablename__ = 'motorists'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)
    data_json = Column(JSON)
    runs = Column()

    def __rep__(self):
        """True, as all users are active."""
        return f"Usr [name={self.name}]"

class Runs(Base):
    """ Tabela relacionada a Motorists 
    """
    __tablename__ = 'runs'
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime, unique=True)
    valor = Column(Integer, nullable=False)
    operation = Column(String)

    