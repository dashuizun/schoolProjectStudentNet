from flask import jsonify, make_response, request, abort
from . import api
from .. import db
from ..models import Community
from ..models import JSONEncoder
from flask_login import current_user
import json

# 获取数据
@api.route('/todo/api/communityApi', methods=['GET'])
def getChuan():
    test_data = Community.query.all()
    tasks = json.loads(json.dumps(test_data, cls=JSONEncoder))
    return jsonify({'tasks': tasks})


# 添加数据
@api.route('/todo/api/addChuan', methods=['POST'], ['GET'])
def addChuan():
    img = request.files.get()
    cname = '游客'
    if current_user.is_authenticated:
        cname = current_user.get_id()
        print('1')

    return ''