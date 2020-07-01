from flask import jsonify, make_response, url_for, g, request, redirect, abort,render_template, flash, session
from . import api
from .. import db
from ..models import User,login_user
from ..models import JSONEncoder
import json



loginnName = [{
    'id': 1,
    'name': '游客',
    'status': False
}]

# 获取数据
@api.route('/todo/api/loginRegistApi', methods=['GET'])
def getLoginRegist():
	return jsonify({'loginName': loginnName})

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
@api.route('/todo/api/loginApi', methods=['GET','POST'])
def login():
	username = request.json.get('name')
	passwor = request.json.get('passwor')
	task = User.query.filter(User.name == username).filter(User.password == passwor).first()

	if task is not None:
		print('ok %s' % username)
		#login_user(task, task)
	#	curr_user = User()
	#	curr_user.name = '1'
		# 生成登录后的session
		# login_user(curr_user)
		#return redirect(url_for('core.index'))
		return jsonify({'code': 200, 'name': username})
	else:
		#flash('账号或密码无效.')
		print('no')
	#return render_template('index.html')
	# return "姓名：%s 密码：%s" % (task.name, task.password)

@api.route('/getLoginApi', methods=['GET','POST'])
def getlogin():
	loginDa = [{
		'name': 'cs'
	}]
	return jsonify(loginnName)
# return jsonify({'status':'no','info':'登录失败'})

	#return jsonify({'status':'no','info':'登录失败'})

