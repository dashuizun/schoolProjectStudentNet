from flask import render_template
from flask_login import login_required, logout_user
from . import main


# 主页
@main.route('/')
def index():
    return render_template('index.html')


# 评论页面
@main.route('/communityHt')
def communityHt():
    return render_template('communityHt.html')


# 市场页面
@main.route('/productHt')
def productHt():
    return render_template('productHt.html')


# 登录页面
@main.route('/login')
def login():
    return render_template('login.html')


# 注册页面
@main.route('/regist')
def regist():
    return render_template('regist.html')


# 测试页面
@main.route('/cs')
def cs():
    return render_template('cs.html')


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return '登出成功!'
