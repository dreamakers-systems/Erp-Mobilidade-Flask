# pylint: disable=too-few-public-methods
""" Objects with flask configurations """

import os


basedir = os.path.abspath(os.path.dirname(__name__))


class Config:
    """Basic configs for all project"""

    SECRET_KEY = os.environ.get("SECRET_KEY")
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = "/media"
    ALLOWED_EXTENSIONS = {
        "txt",
    }


class DevelopmentConfig(Config):
    """Development configs"""

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "dev-data.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """Testing configs"""

    DEBUG = False
    TESTING = True


class ProductionConfig(Config):
    """Production config"""

    DEBUG = False
