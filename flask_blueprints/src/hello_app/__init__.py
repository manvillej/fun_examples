from flask import Blueprint

bp = Blueprint('hello', __name__)

from hello_app import routes