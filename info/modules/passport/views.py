# -*- coding: UTF-8 -*-
# time: 2019/7/29 下午3:50
from io import BytesIO

from flask import request, current_app, abort, make_response, send_file

from info import redis_store, constants
from . import passport_blu
from info.utils.captcha.captcha import captcha
import imghdr

@passport_blu.route('/image_code')
def get_image_code():
    '''
    生成图片验证码
    :return:
    '''
    # 1. 获取参数
    image_Code=request.args.get('image_Code')

    # 2. 校验参数
    if not image_Code:
        return
    # 3. 生成图片验证码
    cid, text, img = captcha.generate_captcha()
    tag = imghdr.what(None, img)
    # 4. 保存图片验证码
    try:
        redis_store.setex('image_'+image_Code,constants.IMAGE_CODE_REDIS_EXPIRES,text)
    except Exception as e:
        return
    # 5.返回图片验证码
    return make_response(send_file(BytesIO(img), mimetype="image/" + tag))

@passport_blu.route('/sms_code',methods=["POST"])
def send_sms_code():
    """

    发送短信的逻辑
    :return:
    """

    # 1.将前端参数转为字典
    mobile = request.json.get("mobile")

    # 2. 校验参数(参数是否符合规则，判断是否有值)
    # 判断参数是否有值
    # 3. 先从redis中取出真实的验证码内容
    # 4. 与用户的验证码内容进行对比，如果对比不一致，那么返回验证码输入错误
    # 5. 如果一致，生成短信验证码的内容(随机数据)
    # 6. 发送短信验证码
    # 保存验证码内容到redis
    # 7. 告知发送结果


@passport_blu.route('/register',methods=["post"])
def register():
    """
    注册功能
    :return:
    """
    # 1. 获取参数和判断是否有值
    # 2. 从redis中获取指定手机号对应的短信验证码的
    # 3. 校验验证码
    # 4. 初始化 user 模型，并设置数据并添加到数据库
    # 5. 保存用户登录状态
    # 6. 返回注册结果