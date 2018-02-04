# Author: c.evan
# -*- coding: utf-8 -*-

import redis

class Config(object):
    #/home/even/Desktop/aa.md 配置数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1/ihome'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SECREK_KEY, redis, Session

    # 配置redis的数据
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # 配置SECREK_KEY
    SECRET_KEY = 'jlhqsDJKREWASDFGJKLNSALFJKLHNSLJFKHGNLMSW'

    # 配置session存储到redis中
    PERMANENT_SESSION_LIFETIME = 86400 # 单位是秒, 设置session过期的时间
    SESSION_TYPE = 'redis' # 指定存储session的位置为redis
    SESSION_USE_SIGNER = True # 对数据进行签名加密, 提高安全性
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 设置redis的ip和端口

class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    # 配置数据库
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1/ihome'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    pass


config_dict = {
    'develop': DevelopmentConfig,
    'product': ProductionConfig
}

