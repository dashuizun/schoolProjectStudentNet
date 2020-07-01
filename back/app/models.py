from . import db
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from datetime import date
from flask import current_app
import json
from . import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import jsonify
app = _Flask(__name__)

# 将数据库数据转换为JSON格式
class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        return json.JSONEncoder.default(self, o)

class Flask(_Flask):
    json_encoder = JSONEncoder

# 设置用户模型
class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(128))
    email = db.Column(db.String(64))


    def __repr__(self):
        return 'User:%s' % self.name

    def keys(self):
        return ['id', 'name', 'password', 'email']

    def __getitem__(self, item):
        return getattr(self, item)


# 登录验证
@login_manager.user_loader
def login_user(user_id):
    return User.query.get(int(user_id))

# 设置评论模型
class Community(db.Model):
    __tablename__ = 'community'
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(64))
    description = db.Column(db.String(128))

    def __repr__(self):
        return 'Community:%s' % self.cname

    def keys(self):
        return ['id', 'cname', 'description']

    def __getitem__(self, item):
        return getattr(self, item)

# 设置市场模型
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    pname = db.Column(db.String(128))
    price = db.Column(db.Integer)
    description = db.Column(db.String(128))

    def __repr__(self):
        return 'Community:%s' % self.name

    def keys(self):
        return ['id', 'name', 'pname', 'price', 'description']

    def __getitem__(self, item):
        return getattr(self, item)

