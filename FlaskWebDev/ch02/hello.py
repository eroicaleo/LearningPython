from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    for key in request.headers:
        print(key, request.headers.get(key))
    return '<h1>Hello World!</h1>' + f'<p>Your browser is {user_agent}.</p>'


@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'
