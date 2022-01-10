# -*- coding: utf-8 -*-
# @Author: Nianko
# @Date:   2022-01-06 17:47:56
# @Last Modified by:   Nianko
# @Last Modified time: 2022-01-10 15:58:16

from flask_restful import fields,reqparse

from app.cat.field import cat_fields
from app.permission.field import role_fields

list_parser = reqparse.RequestParser()
list_parser.add_argument('limit', type=unicode, required=True)
list_parser.add_argument('offset', type=unicode, required=True)

# cat_fields = {
#   'id': fields.Integer,
#   'name': fields.String,
#   'intro': fields.String,
#   'pub_date': fields.String,
#   'icon': fields.String,
#   'video_url': fields.String,
#   'count': fields.Integer,
#   'status': fields.Integer
# }

user_fields = {
  'id': fields.Integer,
  'username': fields.String,
  'nickName': fields.String,
  'avatar': fields.String,
  'roles': fields.List(fields.Nested(role_fields)),
  'owns': fields.List(fields.Nested(cat_fields)),
  'last_login_at': fields.String,
  'created_at': fields.String
}

# user_parser = reqparse.RequestParser()
# user_parser.add_argument('uname', type=unicode, required=True)
# user_parser.add_argument('avatar', type=unicode)
# user_parser.add_argument('tel', type=unicode, required=True)

# me_parser = reqparse.RequestParser()
# me_parser.add_argument('pwd', type=unicode)
# me_parser.add_argument('avatar', type=unicode)

