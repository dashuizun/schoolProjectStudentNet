from flask import Blueprint

api = Blueprint('api', __name__)

from . import communityApi, loginRegistApi, productApi
