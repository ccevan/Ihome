# Author: c.evan
# -*- coding: utf-8 -*-


from . import api
# 需要在其他文件的地方用到数据库, 可能会引发循环导入问题. 因此蓝图模块可以延迟注册
from ihome import db


# 实现蓝图路由
@api.route('/')
def hello_world():
    return 'Hello ihome!'

