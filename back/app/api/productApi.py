from flask import Flask, jsonify,render_template,request,abort,make_response
from flask import jsonify, make_response, request, abort
from . import api
from .. import db
from ..models import Product
from ..models import JSONEncoder
import json

# 添加数据
@api.route('/todo/api/Productions', methods=['GET'])
def getTasks():
	test_data = Product.query.all()
	Production = json.loads(json.dumps(test_data, cls=JSONEncoder))
	return jsonify({'productH': Production})

# 添加数据
@api.route('/todo/api/addProduction', methods=['POST'])
def add_task():
	test_data = Product.query.all()
	Production = json.loads(json.dumps(test_data, cls=JSONEncoder))
	if request.json['name'] == "":
		abort(400)
	task = {
		'id' : Production[-1]['id'] + 1,
		'name': request.json['name'],
		'pname': request.json.get('pname', ""),
		'description' : request.json.get('description', ""),
		'price': request.json.get('price',""),
	}
	tas = Product(id=Production[-1]['id'] + 1, name=request.json['name'], pname=request.json.get('pname', ""),
				  description=request.json.get('description', ""), price=request.json.get('price', ""), )
	db.session.add(tas)
	db.session.commit()
	Production.append(task)
	return jsonify({'productH': Production}), 201

# 删除数据
@api.route('/todo/api/deleteProduction', methods=['POST'])
def delete_task():
	test_data = Product.query.all()
	Production = json.loads(json.dumps(test_data, cls=JSONEncoder))
	task_id = request.json['id']
	for task in Production:
		if task['id'] == task_id:
			Production.remove(task)
			test_data = Product.query.filter(Product.id == task_id).first()
			db.session.delete(test_data)
			db.session.commit()
			return jsonify({'productH': Production})