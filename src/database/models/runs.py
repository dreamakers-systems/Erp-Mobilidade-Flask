from sqlalchemy import String, Column, Integer, DateTime
from src.database import RunsBase


def RunsFactory(name: str):
    """Criar Uma istancia de Runs de Acordo com o nome especifico"""

    class Runs(RunsBase):
        """Tabela relacionada a Motorists"""

        __tablename__ = f"RUNS_{name}"
        id = Column(Integer, primary_key=True)
        date_time = Column(DateTime, unique=True)
        valor = Column(Integer, nullable=False)
        operation = Column(String)
        observation = Column(String)

    return Runs
