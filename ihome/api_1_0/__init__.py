# Author: c.evan
# -*- coding: utf-8 -*-

from flask import Blueprint
# 创建蓝图对象, 并导入子模块
api = Blueprint('api', __name__, url_prefix='/api/v1_0')

import index

