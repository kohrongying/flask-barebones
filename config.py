import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_key')
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    TESTING = False
    DEBUG = False

class StagingConfig(Config):
    TESTING = False
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    TESTING = False
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = False