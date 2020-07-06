from flask import jsonify, request, abort
from . import api
from .. import db
from ..models import Product
from ..models import JSONEncoder
from flask_login import current_user
import json


# 将数据发送到URL地址中
@api.route('/todo/api/Productions', methods=['GET'])
def getTasks():
    # 获取Product表中的所有数据
    test_data = Product.query.all()
    # 将数据库的数据转换为JSON格式
    Production = json.loads(json.dumps(test_data, cls=JSONEncoder))
    # 将数据返回到URL地址中
    return jsonify({'productH': Production})


# 添加数据
@api.route('/todo/api/addProduction', methods=['POST'])
def add_task():
    # 判断登录的用户
    name = '游客'
    if current_user.is_authenticated:
        name = current_user.get_id()
        print('1')
    # 获取数据库数据
    test_data = Product.query.all()
    Production = json.loads(json.dumps(test_data, cls=JSONEncoder))
    if request.json.get('pname', "") == "":
        abort(400)
    task = {
        'id': Production[-1]['id'] + 1,
        'name': name,
        'pname': request.json.get('pname', ""),
        'description': request.json.get('description', ""),
        'price': request.json.get('price', ""),
    }
    # 获取数据 然后 添加到市场模型
    tas = Product(id=Production[-1]['id'] + 1, name=name, pname=request.json.get('pname', ""), description=request.json.get('description', ""), price=request.json.get('price', ""), )
    # 添加数据到数据库中
    db.session.add(tas)
    db.session.commit()
    # 将数据添加到json列表中
    Production.append(task)
    return jsonify({'productH': Production}), 201


# 删除数据
@api.route('/todo/api/deleteProduction', methods=['POST'])
def delete_task():
    # 从数据库中获取数据
    test_data = Product.query.all()
    Production = json.loads(json.dumps(test_data, cls=JSONEncoder))
    # 获取前端中需要删除的数据
    task_id = request.json['id']
    for task in Production:
        if task['id'] == task_id:
            Production.remove(task)
            # 找到该条数据
            test_data = Product.query.filter(Product.id == task_id).first()
            # 删除该条数据
            db.session.delete(test_data)
            db.session.commit()
            return jsonify({'productH': Production})
