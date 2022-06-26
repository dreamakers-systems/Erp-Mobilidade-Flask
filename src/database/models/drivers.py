"""Models for Motorists"""


from sqlalchemy import JSON, Column, Integer, String

from src.database import Base


class Motorists(Base):
    """Motorist Table"""

    __tablename__ = 'motorists'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)
    data_json = Column(JSON)

    def __rep__(self):
        """True, as all users are active."""
        return f'Usr [name={self.name}]'
