# -*- coding: utf-8 -*-
# @Author: Nianko
# @Date:   2022-01-07 10:44:46
# @Last Modified by:   Nianko
# @Last Modified time: 2022-01-07 10:45:20

from flask_restful import fields,reqparse

list_parser = reqparse.RequestParser()
list_parser.add_argument('limit', type=unicode, required=True)
list_parser.add_argument('offset', type=unicode, required=True)

cat_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'intro': fields.String,
    'pub_date': fields.String,
    'icon': fields.String,
    'video_url': fields.String,
    'count': fields.Integer,
    'created_at': fields.String,
    'is_collected': fields.Boolean(default=False),
    'is_visited': fields.Boolean(default=False),
    'is_recommend': fields.Boolean(default=False),
    'status': fields.Integer
}