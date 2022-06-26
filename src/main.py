# pylint: disable=import-outside-toplevel
"""Aplication Factory"""

from flask import Flask


def init_app() -> Flask:
    """init_app é uma fectory que retorna
    uma instancia da aplcação Flask.

    Para configurar a aplicação deve-se Intanciar
    o objeto de configuração de acordo com o ambiente.

    O banco de dodos é manipulado através da biblioteca
    SQLAlchemy. Todos os arquivos para interação com
    o banco de dados esta em ./src/database/, sendo que
    dentro desse diretorio existe outras duas pastas essenciais,
    que são:
    ../models que contens os models da aplicão e
    ../querys que contem as interações com o banco de dados


    SQLAlchemy - Website: https://www.sqlalchemy.org/

    As Blueprints da apicação estão setadas detro de
    ./src/blueprints/blueprint_name/. Cada uma
    possui um url proprio para suas rotas que é
    setado em url_prefix. Ela pode conter um diretorio
    src para manter os objetos utilizados pela blueprints

    """

    app = Flask(__name__)

    # Setando configurações da aplicação
    from .settings import TestingConfig

    app.config.from_object(TestingConfig)

    # Configurando banco de dados
    from .database import Base, DBConnectionHendler

    db_connection = DBConnectionHendler()
    engine = db_connection.get_engine()

    # Criando um contexto para a aplicação.
    # Referencia: https://flask.palletsprojects.com/en/2.1.x/appcontext/
    with app.app_context():

        # Registrando as Blueprints: https://flask.palletsprojects.com/en/2.1.x/blueprints/

        from .blueprints import auth

        app.register_blueprint(auth)

        from .blueprints import dashboard_app

        app.register_blueprint(dashboard_app)

        from .blueprints import drivers_app

        app.register_blueprint(drivers_app)

        from .blueprints import clients_app

        app.register_blueprint(clients_app)

        from .blueprints import revenues_app

        app.register_blueprint(revenues_app)

        # Criando tabelas que não existem e estão
        # presentes na engine.
        Base.metadata.create_all(engine)

        return app
