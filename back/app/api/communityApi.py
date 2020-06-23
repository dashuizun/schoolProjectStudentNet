from flask import jsonify, make_response, request, abort
from . import api
from .. import db
from ..models import Community
from ..models import JSONEncoder
import json

# 获取数据
@api.route('/todo/api/communityApi', methods=['GET'])
def getCommunity():
	test_data = Community.query.all()
	tasks = json.loads(json.dumps(test_data, cls=JSONEncoder))
	return jsonify({'tasks': tasks})

# 添加数据
@api.route('/todo/api/addCommunityApi', methods=['POST'])
def addCommunity():
	test_data = Community.query.all()
	tasks = json.loads(json.dumps(test_data, cls=JSONEncoder))
	if request.json['cname'] == "":
		abort(400)
	task = {
		'id' : tasks[-1]['id'] + 1,
		'cname': request.json['cname'],
		'description': request.json.get('description', ""),
	}
	tas = Community(id= tasks[-1]['id']+1,cname= request.json['cname'],description= request.json.get('description', ""))
	db.session.add(tas)
	db.session.commit()
	tasks.append(task)
	return jsonify({'tasks': tasks}), 201