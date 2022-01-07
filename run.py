# -*- coding: utf-8 -*-
# @Author: Nianko
# @Date:   2022-01-06 14:44:24
# @Last Modified by:   Nianko
# @Last Modified time: 2022-01-07 16:27:04

from flask_script import Manager

from app import app, db

# 追踪所有在命令行中调用的命令和处理过程的调用和运行情况
manager = Manager(app)

if __name__ == '__main__':
    app.debug =True
    app.run()