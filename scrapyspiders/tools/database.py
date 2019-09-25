from databaseconfig import *
from redis import StrictRedis
import pymysql
from pymongo import MongoClient


def get_redis_info():
    return StrictRedis(**REDIS_INF)


def get_mysql_client():
    return pymysql.connect(**MYSQl_INF)

def get_mongo_client():
    return MongoClient(**mongo_info)