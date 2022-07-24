from sqlalchemy import Column, DateTime, Integer, String

from sqlalchemy.ext.declarative import declarative_base



def runs_factory(name: str):
    """Criar Uma istancia de Runs de Acordo com o nome especifico"""
    RunsBase = declarative_base(class_registry=dict())
    

    class Runs(RunsBase):
        """Tabela relacionada a Motorists"""

        __table_args__ = {'extend_existing': True}
        __tablename__ = f'RUNS_{name}'
        id = Column(Integer, primary_key=True)
        date_time = Column(DateTime, unique=True)
        valor = Column(Integer, nullable=False)
        operation = Column(String)
        observation = Column(String)

    return Runs
