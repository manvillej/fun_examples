from src import class_decorator_with_args
from src import func_decorator_with_args
from src import class_decorator_without_args
from src import func_decorator_without_args


@class_decorator_with_args("World 1")
def function1(val):
	return {'val1':val}

@func_decorator_with_args("World 2")
def function2(val):
	return {'val2': val}

@class_decorator_without_args
def function3(val):
	return {'val3': val}
@func_decorator_without_args
def function4(val):
	return {'val4': val}


def main():
	print("function 1: class decorator with args")
	val = function1('test1')
	print(val)
	print("")

	print("function 2: function decorator with args")
	val = function2('test2')
	print(val)
	print("")

	print("function 3: class decorator without args")
	val = function3('test3')
	print(val)
	print("")

	print("function 4: function decorator without args")
	val = function4('test4')
	print(val)


if __name__ == '__main__':
	main()
