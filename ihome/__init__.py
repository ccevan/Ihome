# Author: c.evan
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_dict, Config
#csrf保护, redis, Session
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
import redis

# 为了外界多个文件调用某个对象. 我们可以采取, 先定义, 再创建的方式
# db是需要数据库配置参数的
db = SQLAlchemy()

# 定义CSRF对象
csrf = CSRFProtect()

# 定义redis_store对象, 先设置为None
redis_store = None

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])

    # 为了解决蓝图循环导入的问题, 也可以延迟导入
    from ihome.api_1_0 import api
    app.register_blueprint(api)

    # 某些对象需要外界调用. 可以延迟加载
    db.init_app(app)

    # 创建CSRF对象
    csrf.init_app(app)

    # 创建redis
    global redis_store
    redis_store = redis.StrictRedis(port=Config.REDIS_PORT, host=Config.REDIS_HOST)

    # 创建Session, 将session数据从以前默认的cookie, 存放到redis中
    # http://pythonhosted.org/Flask-Session/ 教程
    Session(app)

    # 这里需要返回APP对象
    return app, db

