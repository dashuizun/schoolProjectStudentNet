from flask import jsonify, make_response, request, abort
from . import api
from .. import db
from ..models import Community
from ..models import JSONEncoder
from flask_login import current_user
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
    cname = '游客'
    if current_user.is_authenticated:
        cname = current_user.get_id()
        print('1')
    test_data = Community.query.all()
    tasks = json.loads(json.dumps(test_data, cls=JSONEncoder))
    task = {
        'id': tasks[-1]['id'] + 1,
        'cname': cname,
        'description': request.json.get('description', ""),
    }
    tas = Community(id=tasks[-1]['id'] + 1, cname=cname, description=request.json.get('description', ""))
    db.session.add(tas)
    db.session.commit()
    tasks.append(task)
    return jsonify({'tasks': tasks}), 201
