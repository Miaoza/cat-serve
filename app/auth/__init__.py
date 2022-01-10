# -*- coding: utf-8 -*-
# @Author: Nianko
# @Date:   2022-01-10 10:24:33
# @Last Modified by:   Nianko
# @Last Modified time: 2022-01-10 14:14:21

from login import *

auth_api.add_resource(Register, '/register')
auth_api.add_resource(Login, '/login')
# user_api.add_resource(UsersTable, '/admin/users')
# user_api.add_resource(UsersTableView, '/admin/users/<int:user_id>')
# user_api.add_resource(Users, '/users')
# user_api.add_resource(UserView, '/users/<int:user_id>')
# user_api.add_resource(Me, '/me')