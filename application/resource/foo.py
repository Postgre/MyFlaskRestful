# _*_ coding:utf-8 _*_
import json
from bson import json_util

from flask import request
from flask_restful import Resource, reqparse

from application.database import db_mongo, db_sqlite
from application.database import Person, Computer


parser = reqparse.RequestParser()
parser.add_argument('task', required=True, location='json', help='receive a json data')


class TestMongo(Resource):
    def get(self):
        result = db_mongo.product.find_one()
        return json.loads(json_util.dumps(result))

    def post(self):
        db_mongo.product.insert_one(request.json)
        return 'Insert one success'

    def put(self):
        db_mongo.product.update(request.json, {"$set": {"price": "0"}})
        return 'Update success'

    def delete(self):
        data = request.json['data']
        db_mongo.product.remove({"data": data})
        return 'Delete success'


class TestSqlite(Resource):
    def get(self):
        person = Person.query.all()
        result = [psn.to_json() for psn in person]
        return result


