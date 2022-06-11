from sqlalchemy import Column, Integer, String

from src.database import Base


class RevenuesPorcents(Base):
    """Tabela relacionada a Motorists"""

    __tablename__ = 'porcents'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    porcent_one = Column(Integer, nullable=False)
    porcent_two = Column(Integer, nullable=False)
    porcent_tree = Column(Integer, nullable=False)
