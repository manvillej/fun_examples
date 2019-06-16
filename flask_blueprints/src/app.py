from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Welcome"

from error_app import bp as errors_bp
app.register_blueprint(errors_bp)


from hello_app import bp as hello_bp
app.register_blueprint(hello_bp)