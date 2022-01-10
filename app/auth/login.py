# -*- coding: utf-8 -*-
# @Author: Nianko
# @Date:   2022-01-10 10:24:39
# @Last Modified by:   Nianko
# @Last Modified time: 2022-01-10 16:18:06

from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api, marshal
from enum import Enum
import random
import string

from app import db
from app.user.model import User
from fields import *
from app.user.fields import user_fields
# from app.auth.auth import *
# from app.auth.admin_auth import *

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
auth_api = Api(auth_bp)

class System(Enum):
  ADMIN = 1
  FRONT = 2

def getDefaultPwd():
  letters = string.ascii_letters+string.digits
  return "".join([random.choice(letters) for i in range(10)])


class Register(Resource):
  def post(self):
    pass

class AdminRegister(Resource):
  def post(self):
    args = admin_register_parser.parse_args()
    phone = args['phone']
    username = args['phone']
    pwd = getDefaultPwd()
    # User()
    pass

class Login(Resource):
  def post(self):
    args = login_parser.parse_args()
    phone = args['phone']
    pwd = args['password']
    system = System[args['system']].value # 【front,admin】
    user = User.query.filter(User.phone == phone).first()
    if user and user.check_password(pwd):
      token = user.generate_auth_token(system) #token
      # user = marshal(user, user_fields)
      return jsonify({"code": 0, "data": token})
    else:
      return jsonify({"code": -1, "message": "账号或密码错误"})

class Me(Resource):
  def get(self):
    auth = request.authorization
    me = User.verify_auth_token(auth.id, auth.token)
    me = marshal(me, user_fields)
    return jsonify({"code": 1, "data": me})