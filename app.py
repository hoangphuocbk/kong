# flask_web/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/chaio')
def hello_world():
    return 'Hello, Docker!'

@app.route('/greet')
def greet_func():
    return 'Hello, This is /greet !'