from os import getenv


SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg2://user:password@pg/postgres",
)


class Config:
    DEBUG = False
    TESTING = False
    ENV = "development"

    SECRET_KEY = '\xca|\xa3\xb9\x87>\xbdN\xf2\xa7\xf9j\xb1\x81B\x91\xce\xfb\te\xa8\xfb\x8b\xe4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    ENV = "production"
    SECRET_KEY = '\x99<\x95\xdd\x8e\x03\xa2C\xbeYo\x00v%j\x95\xbc\xbf\x02\xa2V\xfd`\xaf'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True