from flask import jsonify, make_response, request, abort
from . import api

#模拟json数据
tasks = [
    {
		'id': 1,
		'title': '张三',
		'description': '这网站真好用',
        'done': False
    },
    {
		'id': 2,
		'title': '王五',
		'description': '这网站真的太好用了',
        'done': False
    }
]
#GET方法api
@api.route('/todo/api/tasks', methods=['GET'])
def getTasks():
	return jsonify({'tasks': tasks})

#POST方法API，添加数据项
@api.route('/todo/api/addTask', methods=['POST'])
def add_task():
	if request.json['title'] == "":
		abort(400)
	task = {
		'id' : tasks[-1]['id'] + 1,
		'title': request.json['title'],
		'description' : request.json.get('description', ""),
		'done' : False
	}
	tasks.append(task)
	return jsonify({'tasks': tasks}), 201

#POST方法API，删除数据项
@api.route('/todo/api/deleteTask', methods=['POST'])
def delete_task():
	task_id = request.json['id']
	for task in tasks:
		if task['id'] == task_id:
			tasks.remove(task)
			return jsonify({'tasks': tasks}), 201

#404
@api.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)
