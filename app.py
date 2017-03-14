# _*_ utf-8 _*_
from flask import Flask
from flask_restful import Api

from foo import TestMongo, TestSqlite

app = Flask(__name__)

api_foo = Api(app)
api_foo.add_resource(TestMongo, '/test/1/')
api_foo.add_resource(TestSqlite, '/test/2/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)