from flask import render_template,jsonify
from . import main
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from app.api.communityApi import getTasks


@main.route('/')
def index():
    getTasks()
    return render_template('index.html')

