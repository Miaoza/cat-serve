# -*- coding: utf-8 -*-
# @Author: Nianko
# @Date:   2022-01-10 15:12:36
# @Last Modified by:   Nianko
# @Last Modified time: 2022-01-10 15:58:24

from flask_restful import fields,reqparse

permission_parser = reqparse.RequestParser()
permission_parser.add_argument('page', type=int, required=True)
permission_parser.add_argument('size', type=int, required=True)
permission_parser.add_argument('name', type=str)

permission_group_parser = reqparse.RequestParser()
permission_group_parser.add_argument('page', type=int, required=True)
permission_group_parser.add_argument('size', type=int, required=True)
permission_group_parser.add_argument('name', type=str)

role_parser = reqparse.RequestParser()
permission_group_parser.add_argument('page', type=int, required=True)
permission_group_parser.add_argument('size', type=int, required=True)
permission_group_parser.add_argument('name', type=str)

role_fields = {
  'id': fields.Integer,
  'name': fields.String
}