# -*- coding: UTF-8 -*-
# time: 2019/7/29 上午8:51
from . import index_blu


# 测试
@index_blu.route('/')
def index():
    return '<h1>index-text</h1>'