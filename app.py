#!/usr/bin/env python
# -*- coding:utf-8 -*-



from flask import Flask
from flask import render_template

import pymysql

app = Flask(__name__,template_folder='app/templates')

#主页
@app.route('/', methods=['GET', 'POST'])
def index():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='studentsystem', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM users"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return render_template('index.html',u=u)

#登录页面
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

#注册页面
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return render_template('signin.html')




if __name__ == '__main__':
    app.run(debug=True)