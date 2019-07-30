# -*- coding: UTF-8 -*-
# time: 2019/7/29 下午3:49
from flask import Blueprint


passport_blu=Blueprint('passport', __name__,url_prefix='/passport')

from .views import *