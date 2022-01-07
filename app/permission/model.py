# -*- coding: utf-8 -*-
# @Author: Nianko
# @Date:   2022-01-07 17:34:43
# @Last Modified by:   Nianko
# @Last Modified time: 2022-01-07 18:04:51

from app import db

# 权限
class Permission(db.model):
  __tablename__ = 'permission'
  __table_args__ = {
    "mysql_engine": "InnoDB", # 指定表的引擎,InnoDB（MySQL的数据库引擎之一）
    "mysql_charset": "utf8" # 指定表的编码格式
  }
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80))
  code = db.Column(db.String(80), unique=True)
  creator_id = db.Column(db.Integer) # 创建人
  modifier_id = db.Column(db.Integer) # 修改人

# 权限组
class PermissionGroup(db.model):
  __tablename__ = 'permission_group'
  __table_args__ = {
    "mysql_engine": "InnoDB", # 指定表的引擎,InnoDB（MySQL的数据库引擎之一）
    "mysql_charset": "utf8" # 指定表的编码格式
  }
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80))

# 角色
class Role(db.model):
  __tablename__ = 'role'
  __table_args__ = {
    "mysql_engine": "InnoDB",
    "mysql_charset": "utf8"
  }
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80))