# -*- coding: utf-8 -*-
# @Author: Nianko
# @Date:   2022-01-07 10:44:40
# @Last Modified by:   Nianko
# @Last Modified time: 2022-01-07 13:53:38

from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api, marshal

from app import db
# from app.auth.auth import *
# from app.auth.admin_auth import *
from model import Cat
from fields import *
# from app.user.model import User

front_cat_bp = Blueprint('cats', __name__, url_prefix='/cats') # 创建蓝图
font_cat_api = Api(front_cat_bp)

class Cats(Resource):
    @required_admin_auth
    def get(self):
        pass

    @required_admin_auth
    def post(self):
        pass