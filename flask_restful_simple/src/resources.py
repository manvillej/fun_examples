from flask import request
from flask_restful import Resource, abort

todos = {}

def abort_if_todo_doesnt_exist(func):
	def inner(self, todo_id):
		if todo_id not in todos:
			abort(404, message=f"Todo {todo_id} doesn't exist")
		return func(self, todo_id)
	return inner


class TodoList(Resource):
	def get(self):
		return todos

class Todo(Resource):
	@abort_if_todo_doesnt_exist
	def get(self, todo_id):
		return {todo_id: todos[todo_id]}

	@abort_if_todo_doesnt_exist
	def delete(self, todo_id):
		del todos[todo_id]
		return '', 204

	def put(self, todo_id):
		todos[todo_id] = request.form['data']
		return {todo_id: todos[todo_id]}

