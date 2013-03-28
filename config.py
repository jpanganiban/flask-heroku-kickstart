class Config(object):
    SECRET_KEY = '27ccc159468b4d9f944347ca634ca2a9'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'


class ProductionConfig(Config):
    pass
