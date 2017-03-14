# _*_ coding:utf-8 _*_
from pymongo import MongoClient

con = MongoClient(host='192.168.116.128', port=27017)
db = con.runoob
