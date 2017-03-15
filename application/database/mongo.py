# _*_ coding:utf-8 _*_
from pymongo import MongoClient

from config import load_config

config = load_config()

con = MongoClient(host=config.MONGO_HOST, port=config.MONGO_PORT)
db = con.runoob
