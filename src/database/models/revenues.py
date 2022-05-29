from sqlalchemy import Column, Integer, String

from src.database import Base


class RevenuesPorcents(Base):
    """Tabela relacionada a Motorists"""

    __tablename__ = 'porcents'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    porcent_one = Column(Integer)
    porcent_two = Column(Integer)
    porcent_tree = Column(Integer)
