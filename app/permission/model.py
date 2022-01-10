# -*- coding: utf-8 -*-
# @Author: Nianko
# @Date:   2022-01-07 17:34:43
# @Last Modified by:   Nianko
# @Last Modified time: 2022-01-10 15:43:54

from app import db

# 权限组-权限表
permission_group_permission = db.Table('permission_group_permission', 
  db.Column('permission_group_id', db.Integer, db.ForeignKey('permission_group.id')),
  db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'))
)

# 角色-权限组表
role_permission_group = db.Table('role_permission_group', 
  db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
  db.Column('permission_group_id', db.Integer, db.ForeignKey('permission_group.id'))
)

# 权限
class Permission(db.Model):
  __tablename__ = 'permission'
  __table_args__ = {
    "mysql_engine": "InnoDB", # 指定表的引擎,InnoDB（MySQL的数据库引擎之一）
    "mysql_charset": "utf8" # 指定表的编码格式
  }
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80))
  code = db.Column(db.String(80), unique=True)
  creator_id = db.Column(db.Integer, db.ForeignKey('user.id')) # 创建人
  modifier_id = db.Column(db.Integer, db.ForeignKey('user.id')) # 修改人
  parent_id = db.Column(db.Integer)
  remark = db.Column(db.String(80))

# 权限组
class PermissionGroup(db.Model):
  __tablename__ = 'permission_group'
  __table_args__ = {
    "mysql_engine": "InnoDB", # 指定表的引擎,InnoDB（MySQL的数据库引擎之一）
    "mysql_charset": "utf8" # 指定表的编码格式
  }
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80))
  creator_id = db.Column(db.Integer, db.ForeignKey('user.id')) # 创建人
  modifier_id = db.Column(db.Integer, db.ForeignKey('user.id')) # 修改人

# 角色
class Role(db.Model):
  __tablename__ = 'role'
  __table_args__ = {
    "mysql_engine": "InnoDB",
    "mysql_charset": "utf8"
  }
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80))
  creator_id = db.Column(db.Integer, db.ForeignKey('user.id')) # 创建人
  modifier_id = db.Column(db.Integer, db.ForeignKey('user.id')) # 修改人