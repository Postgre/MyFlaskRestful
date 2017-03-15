# _*_ utf-8 _*_
import sys
import os

# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from flask import Flask
from flask_restful import Api

from config import load_config
from .resource.foo import TestMongo, TestSqlite
from database import db_sqlite


def create_app():
    app = Flask(__name__)
    app.config.from_object(load_config())

    register_db(app)
    register_api_foo(app)

    return app


def register_db(app):
    db_sqlite.init_app(app)


def register_api_foo(app):
    api_foo = Api(app)
    api_foo.add_resource(TestMongo, '/test/mongo')
    api_foo.add_resource(TestSqlite, '/test/sqlite')