# -*- coding: utf-8 -*-
# @Author: Nianko
# @Date:   2022-01-06 17:47:46
# @Last Modified by:   Nianko
# @Last Modified time: 2022-01-07 14:49:28

from app import db

class User(db.model):
  __tablename__ = 'user'
  __table_args__ = {
    "mysql_engine": "InnoDB",
    "mysql_charset": "utf8"
  }
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  phone = db.Column(db.String(11), unique=True)
  email = db.Column(db.String(120))
  remark = db.Column(db.Text)
  create_date = db.Column(db.DateTime) # 创建时间
  update_date = db.Column(db.DateTime) #更新时间

  def __init__(self, name, phone):
    self.name = name
    self.phone = phone

  def __repr__(self):
    return '<User %r>' % self.username