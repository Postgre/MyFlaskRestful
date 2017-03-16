# _*_ coding:utf-8 _*_
import os

from default import config


class DevelopmentConfig(config):
    MONGO_URI = ''
    MONGO_HOST = '192.168.116.128'
    MONGO_PORT = 27017

    SQLALCHEMY_DATABASE_URI = "mysql://zhongkang:wocapwc@192.168.116.128/test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    DEBUG = True
    HOST = '0.0.0.0'

