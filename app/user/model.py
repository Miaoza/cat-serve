# -*- coding: utf-8 -*-
# @Author: Nianko
# @Date:   2022-01-06 17:47:46
# @Last Modified by:   Nianko
# @Last Modified time: 2022-01-07 17:49:35

from app import db

# 猫和铲屎官 多对多关系
owns = db.Table('owns',
    db.Column('cat_id', db.Integer, db.ForeignKey('cat.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

# 用户-角色表
user_role = db.Table('user_role', 
  db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
  db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

class User(db.model):
  __tablename__ = 'user'
  __table_args__ = {
    "mysql_engine": "InnoDB",
    "mysql_charset": "utf8"
  }
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True) # 用户名
  password = db.Column(db.String(80)) # 密码
  nick_name = db.Column(db.String(80)) # 昵称
  phone = db.Column(db.String(11), unique=True) # 电话
  owns = db.relationship('Cat', secondary=owns, backref=db.backref('user', lazy='dynamic')) # 拥有的猫孩子
  roles = db.relationship('Role', secondary=user_role, backref=db.backref('user', lazy='dynamic'))
  remark = db.Column(db.Text) # 备注
  login_date = db.Column(db.DateTime) # 登录时间
  create_date = db.Column(db.DateTime) # 创建时间
  update_date = db.Column(db.DateTime) # 更新时间

  def __init__(self, username, phone):
    self.username = username
    self.phone = phone

  def __repr__(self):
    return '<User %r>' % self.username
