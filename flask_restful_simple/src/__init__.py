from flask import Flask, request
from flask_restful import Resource, Api
from .resources import TodoList, Todo

app = Flask(__name__)
api = Api(app)

api.add_resource(TodoList, '/')
api.add_resource(Todo, '/<string:todo_id>')
