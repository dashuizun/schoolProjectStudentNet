from flask import jsonify, make_response, url_for, g, request, redirect, abort,render_template, flash, session, request, redirect, url_for, render_template, flash
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from . import api
from .. import db
from ..models import User
from ..models import JSONEncoder
from .. import login_manager
import json

# 获取数据
@api.route('/todo/api/getLoginApi', methods=['GET'])
def getLogin():
    loginnName = [{'lname': '游客'}]
    if current_user.is_authenticated:
        loginnName[0]['lname'] = current_user.get_id()
        print('1')
    return jsonify({'loginnName': loginnName})

# 添加数据
@api.route('/todo/api/addRegistApi', methods=['POST'])
def addRegist():
	test_data = User.query.all()
	tasks = json.loads(json.dumps(test_data, cls=JSONEncoder))
	if request.json['name'] == "":
		abort(400)
	task = {
		'id' : tasks[-1]['id'] + 1,
		'name': request.json['name'],
        'password': request.json.get('passwor', ""),
		'email': request.json.get('email', ""),
	}
	tas = User(id= tasks[-1]['id']+1,name= request.json['name'],
               password= request.json.get('passwor', ""),email= request.json.get('email', ""))
	db.session.add(tas)
	db.session.commit()
	tasks.append(task)
	return jsonify({'tasks': tasks}), 201


# 数据
# json.dumps(loginnName[0]['name'], ensure_ascii=False)

@login_manager.user_loader
def load_user(user_id):
    if query_user(user_id) is not None:
        curr_user = User()
        curr_user.id = user_id
        return curr_user


@api.route('/cscscs')
@login_required
def cscscs():
    return '当前用户: %s' % current_user.get_id()


@api.route('/todo/api/loginApi', methods=['GET','POST'])
def login():
    if request.method == 'POST':

        user_id = request.json.get('name')
        user_pw = request.json.get('passwor')
        user = query_user(user_id)
        if user is not None and user_pw == user['password']:
            print('信息----------成功登陆------------')
            curr_user = User()
            curr_user.id = user_id
            # 通过Flask-Login的login_user方法登录用户
            login_user(curr_user)
            # loginnName[0]['name'] = user_id
            return jsonify({'code': 200, 'name': user_id})

    # GET 请求
    return 'cs %s' % current_user.get_id()

def query_user(user_name):
    for user in json.loads(json.dumps(User.query.all(), cls=JSONEncoder)):
        if user_name == user['name']:
            return user
