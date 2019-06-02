# decorators

just a bunch of example decorators. there seems to be 2 categorizations of decorators: funcs vs classes and args vs no args

the funcs vs classes seem pretty straight forward. One uses defines the decorator as a class and the other as a function.

the args vs no args is whether the decorator takes arguments at the time of definitions for example:
> @decorator_no_args()
> def hello():
>	pass

vs.

> @decorator_args(arg1, arg2)
> def hello():
>	pass