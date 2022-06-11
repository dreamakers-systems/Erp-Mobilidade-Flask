# pylint: disable=too-few-public-methods
"""Configurações para o projeto
Para passar determinadas variaveis e constantes para o sistemas
esteremos utilizando objetos com diferentes propriedades para
cada ambiente. Para setar esse ambiente va para
"""

import getpass
import os
from os.path import join

from dotenv import load_dotenv


class Config:
    """Configurações globais para todo o projeto"""

    user_dir = join(
        '/home', getpass.getuser(), 'vars_apps', '.env_erp_mobilidade'
    )
    load_dotenv(user_dir)

    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOAD_FOLDER = '/media'
    ALLOWED_EXTENSIONS = {
        'txt',
    }
    DATABASE_CONNECTION = os.environ.get('DATABASE_CONNECTION')


class TestingConfig(Config):
    """Ambiente de testes"""

    DEBUG = False
    TESTING = True


class ProductionConfig(Config):
    """Ambiente de produção"""

    DEBUG = False
