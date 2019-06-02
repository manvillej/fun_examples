


# class decorator
class class_decorator_with_args(object):
	"""
	example:
	> @class_decorator_with_args("World")
	> def test(value):
	>	return {'val':value}
	>value = test('test')
	Hello World
	>value
	{'val':'test'}
	"""
	def __init__(self, name):
		self.name = name

	def __call__(self, func):

		def wrapped_func(*args):
			print(f'Hello {self.name}')
			return func(*args)
		return wrapped_func
	
# function decorator
def func_decorator_with_args(name):
	"""	
	example:
	> @func_decorator_with_args("World")
	> def test(value):
	>	return {'val':value}
	>value = test('test')
	Hello World
	>value
	{'val':'test'}
	"""
	def wrap(func):
		def wrapped_func(*args):
			print(f'Hello {name}')
			return func(*args)
		return wrapped_func
	return wrap

class class_decorator_without_args(object):
	"""
	example:
	> @func_decorator_with_args()
	> def test(value):
	>	return {'val':value}
	>value = test('test')
	Hello World
	>value
	{'val':'test'}
	"""
	def __init__(self, func):
		self.func = func

	def __call__(self, *args):
		print("Hello World")
		self.func(*args)

def func_decorator_without_args(func):
	"""
	example:
	> @func_decorator_with_args()
	> def test(value):
	>	return {'val':value}
	>value = test('test')
	Hello World
	>value
	{'val':'test'}
	"""
	def new_func(*args):
		print("Hello World")
		return func(*args)
	return new_func
