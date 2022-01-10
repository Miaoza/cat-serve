# -*- coding: utf-8 -*-
# @Author: Nianko
# @Date:   2022-01-10 10:24:44
# @Last Modified by:   Nianko
# @Last Modified time: 2022-01-10 16:01:07

from flask_restful import fields,reqparse

register_parser = reqparse.RequestParser()
register_parser.add_argument('phone', type=str, required=True)
register_parser.add_argument('password', type=str, required=True)
register_parser.add_argument('rePassword', type=str, required=True)
# 多个值&列表
register_parser.add_argument('roles', type=str, required=True, action='append')
register_parser.add_argument('username', type=str, required=True)
register_parser.add_argument('nickName', type=str, required=False)
register_parser.add_argument('avatar', type=str, required=False)

admin_register_parser = reqparse.RequestParser()
admin_register_parser.add_argument('phone', type=str, required=True)
admin_register_parser.add_argument('username', type=str)


login_parser = reqparse.RequestParser()
login_parser.add_argument('phone', type=str, required=True)
login_parser.add_argument('password', type=str, required=True)
login_parser.add_argument('system', type=int, required=True)
