# -*- coding: utf-8 -*-
# @Author: Nianko
# @Date:   2022-01-10 15:06:44
# @Last Modified by:   Nianko
# @Last Modified time: 2022-01-10 16:34:17

from app.user.model import User
# from app.permission.model import Role
from app import db

# db.drop_all()
# db.create_all()

# role = Role(name='admin')
# db.session.add(role)
# db.session.commit()
# db.session.close()

admin_user = User(phone="13000000000", password="Abc123456!", username='admin')
db.session.add(admin_user)
db.session.commit()
db.session.close()