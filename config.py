# -*- coding: utf-8 -*-
# @Author: Nianko
# @Date:   2022-01-06 16:10:56
# @Last Modified by:   Nianko
# @Last Modified time: 2022-01-07 09:46:59

class Config(object):
    # True: Flask-SQLAlchemy 将会追踪对象的修改并且发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:CEChealth123456!@127.0.0.1/catdb?charset=utf8'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:CEChealth123456!@127.0.0.1/catdb?charset=utf8'

class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:CEChealth123456!@127.0.0.1/catdb?charset=utf8'


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': ProductionConfig,
}