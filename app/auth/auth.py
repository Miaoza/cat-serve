# -*- coding: utf-8 -*-
# @Author: Nianko
# @Date:   2022-01-10 13:46:03
# @Last Modified by:   Nianko
# @Last Modified time: 2022-01-10 13:58:54

from app import app
from app.user import User

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(token):
  user = User.verify_auth_token(token)
  return user