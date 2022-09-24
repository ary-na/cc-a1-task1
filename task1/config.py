import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '57e19ea558d4967a552d03deece34a70'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # os.environ[
    #     "GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/ariannajafiyamchelo/Downloads/cc-a1-task1-362004-168dad8f4b0c.json"


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    HOST = '127.0.0.1'
    PORT = 8080
    DEBUG = True
