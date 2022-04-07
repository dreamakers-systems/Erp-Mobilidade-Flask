# pylint: disable=import-outside-toplevel
""" Aplication Factory """

from flask import Flask, request, make_response
from flask_cors import CORS


def init_app():
    " Factory method for create the Flask App "
    app = Flask(__name__,)
    cors_origin = [
        'http://192.168.0.105:3000',
        'http://localhost:3000'
    ]

    CORS(
        app,
        resources={r"/motorists/*": {"origins": cors_origin}},
        supports_credentials=True,)

    ### CORS section
    @app.after_request
    def after_request_func(response):
        origin = request.headers.get('Origin')
        if request.method == 'OPTIONS':
            response = make_response()
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            response.headers.add('Accept-Language', 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3')
            response.headers.add('Accept-Encoding', 'gzip, deflate')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type, authorization, x-csrf-token')
            response.headers.add('Access-Control-Request-Headers', 'Content-type')

            response.headers.add('Access-Control-Allow-Methods',
                                'GET, POST, OPTIONS, PUT, PATCH, DELETE')

            response.headers.add('Access-Control-Allow-Origin', origin)

        return response
    ### end CORS section
    from .settings import Config
    app.config.from_object(Config)

    # Database
    from .database import DBConnectionHendler
    from .database import Base

    db_connection = DBConnectionHendler()
    engine = db_connection.get_engine()


    with app.app_context():

        # from .core import auth
        # app.register_blueprint(auth)

        from .blueprints import motorist_app
        app.register_blueprint(motorist_app)

        from .blueprints import clients_app
        app.register_blueprint(clients_app)

        from .blueprints import revenues_app
        app.register_blueprint(revenues_app)

        Base.metadata.create_all(engine)

        return app

        
