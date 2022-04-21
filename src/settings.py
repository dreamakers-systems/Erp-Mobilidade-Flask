# pylint: disable=too-few-public-methods
""" Configurações para o projeto 
Para passar determinadas variaveis e constantes para o sistemas 
esteremos utilizando objetos com diferentes propriedades para 
cada ambiente. Para setar esse ambiente va para 
"""

import os


basedir = os.path.abspath(os.path.dirname(__name__))


class Config:
    """Configurações globais para todo o projeto"""

    SECRET_KEY = os.environ.get("SECRET_KEY")
    UPLOAD_FOLDER = "/media"
    ALLOWED_EXTENSIONS = {
        "txt",
    }


class DevelopmentConfig(Config):
    """ Ambiente de desenvolvimento"""

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "dev-data.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """ Ambiente de testes """

    DEBUG = False
    TESTING = True


class ProductionConfig(Config):
    """ Ambiente de produção """

    DEBUG = False
