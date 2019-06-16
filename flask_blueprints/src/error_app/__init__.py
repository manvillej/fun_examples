from flask import Blueprint

bp = Blueprint('errors', __name__)

from error_app import handlers