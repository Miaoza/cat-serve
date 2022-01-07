# -*- coding: utf-8 -*-
# @Author: Nianko
# @Date:   2022-01-07 09:48:36
# @Last Modified by:   Nianko
# @Last Modified time: 2022-01-07 17:03:13

from app import db

class Cat(db.model):
  __tablename__ = 'cat'
  __table_args__ = {
    "mysql_engine": "InnoDB", # 指定表的引擎,InnoDB（MySQL的数据库引擎之一）
    "mysql_charset": "utf8" # 指定表的编码格式
  }
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80)) # 姓名
  avatar = db.Column(db.Text) # 头像
  grender = db.Column(db.String(8)) # 性别 【男、女】
  birth = db.Column(db.Integer) # 生日 时间戳
  weight = db.Column(db.Integer) # 体重
  sterilization = db.Column(db.Integer) # 绝育 【0:没有，1:已绝育】
  nationality = db.Column(db.String(80)) # 国籍
  character = db.Column(db.String(80)) # 性格
  favorite_food = db.Column(db.String(80)) # 最爱的食物
  health = db.Column(db.Integer) # 健康状况【0: 健康，1:不健康】
  address = db.Column(db.Text) # 住址
  photo_album = db.relationship('PhotoAlbum', backref='cat', lazy='dynamic') # 相册
  intro = db.Column(db.Text) # 介绍
  remark = db.Column(db.String(80)) # 备注
  create_date = db.Column(db.DateTime) # 创建时间
  update_date = db.Column(db.DateTime) #更新时间

  # 默认构造方法
  def __init__(self):
    pass

  #repr()方法显示一个可读字符串，虽然不是完全必要，不过用于调试和测试还是很不错的。
  def __repr__(self):
    return '<Cat %r>' % self.name

# 特征
class Characteristic(db.model):
  __tablename__ = 'characteristic'
  __table_args__ = {
    "mysql_engine": "InnoDB",
    "mysql_charset": "utf8"
  }
  id = db.Column(db.Integer, primary_key=True)
  variety = db.Column(db.String(80)) # 品种
  color = db.Column(db.String(80)) # 颜色
  somatotype = db.Column(db.String(8)) # 体型 【大、中、小】
  fur_size = db.Column(db.String(8)) # 毛长短 【长、短】
  remark = db.Column(db.String(80)) # 备注
  create_date = db.Column(db.DateTime) # 创建时间
  update_date = db.Column(db.DateTime) #更新时间

# 相册
class PhotoAlbum(db.model):
  __tablename__ = 'photo_album'
  __table_args__ = {
    "mysql_engine": "InnoDB",
    "mysql_charset": "utf8"
  }
  id = db.Column(db.Integer, primary_key=True)
  url = db.Column(db.Text)
  cat_id = db.Column(db.Integer, db.ForeignKey('cat.id'))
  status = db.Column(db.Integer) # 状态 【0:待使用，1: 使用中】
  remark = db.Column(db.String(80)) # 备注
  create_date = db.Column(db.DateTime) # 创建时间
  update_date = db.Column(db.DateTime) #更新时间