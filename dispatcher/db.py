from redis import StrictRedis

from databaseconfig import *


def get_redis():
    return StrictRedis(**REDIS_INF)
