# pylint: disable=too-few-public-methods
"""Configurações para o projeto
Para passar determinadas variaveis e constantes para o sistemas
esteremos utilizando objetos com diferentes propriedades para
cada ambiente. Para setar esse ambiente va para
"""

import os
from os.path import abspath, basename, dirname, join

from dotenv import load_dotenv

basedir = abspath(dirname(__name__))
dotenv_path = join(basedir, '.env')
load_dotenv(dotenv_path)


class Config:
    """Configurações globais para todo o projeto"""

    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOAD_FOLDER = '/media'
    ALLOWED_EXTENSIONS = {
        'txt',
    }
    DATABASE_CONNECTION = os.environ.get('DATABASE_CONNECTION')


class DevelopmentConfig(Config):
    """Ambiente de desenvolvimento"""

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        basedir, 'dev-data.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """Ambiente de testes"""

    DEBUG = False
    TESTING = True


class ProductionConfig(Config):
    """Ambiente de produção"""

    DEBUG = False
