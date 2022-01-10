# -*- coding: utf-8 -*-
# @Author: Nianko
# @Date:   2022-01-06 17:47:46
# @Last Modified by:   Nianko
# @Last Modified time: 2022-01-10 16:37:34

# from flask_httpauth import HTTPTokenAuth
# 转换密码用到的库
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime

from app import app, db
from app.cat.model import Cat
from app.permission.model import Role

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

class User(db.Model):
  __tablename__ = 'user'
  __table_args__ = {
    "mysql_engine": "InnoDB",
    "mysql_charset": "utf8"
  }
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), nullable=False) # 用户名
  pwd_hash = db.Column(db.String(255), nullable=False) # hash后的密码
  phone = db.Column(db.String(11), unique=True, nullable=False) # 电话
  nick_name = db.Column(db.String(80)) # 昵称
  owns = db.relationship('Cat', secondary=owns, backref=db.backref('user', lazy='dynamic')) # 拥有的猫孩子
  roles = db.relationship('Role', secondary=user_role, backref=db.backref('user', lazy='dynamic'))
  remark = db.Column(db.Text) # 备注
  login_date = db.Column(db.DateTime, default=datetime.now) # 登录时间
  create_date = db.Column(db.DateTime, default=datetime.now) # 创建时间
  update_date = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now) # 更新时间

  # def __init__(self, phone, password, username):
  #   self.phone = phone
  #   self.password = password
  #   self.username = username

  def __repr__(self):
    return '<User %r>' % self.username

  @property
  def password(self):
    raise AttributeError("密码不允许读取")

  # 转换密码为hash存入数据库
  @password.setter
  def password(self, password):
    self.pwd_hash = generate_password_hash(password)

  # 检查密码
  def check_password(self, password):
    return check_password_hash(self.pwd_hash, password)

  # 实例化一个签名序列化对象 serializer，有效期 100 分钟
  def generate_auth_token(self, expiration=6000, system=''):
    s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({"id": self.id, system: system})

  # 声明一个静态方法，不可以引用类中的属性或方法，其参数列表也不需要约定的默认参数self
  @staticmethod
  # 回调函数，对 token 进行验证
  def verify_auth_token(token, system):
    s = Serializer(app.config['SECRET_KEY'])
    try:
      data = s.loads(token)
    except:
      return None # invalid token
    # if(data['system'] == system):
    #   user = User.query.get(data['id'])
    #   return user
    user = User.query.get(data['id'])
    return user
