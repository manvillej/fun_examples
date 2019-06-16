from flask import render_template
from hello_app import bp

@bp.route('/hello/')
@bp.route('/hello/<name>')
def hello(name='World'):
	return render_template('hello_app/hello.html', name=name)