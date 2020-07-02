from flask import Flask
from .config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = '请登录'

def create_app(config_name):
    # 配置Flask静态目录、URL目录
    app = Flask(__name__,template_folder='../../front',static_url_path='',static_folder='../../front')
    # 导入配置文件
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # 配置数据库
    db.init_app(app)
    # 登录
    login_manager.init_app(app)
    # 配置文件蓝图
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)
    # 返回app
    return app