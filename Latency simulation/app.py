from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    time.sleep(5)
    return 'Hello, World!'

@app.route('/hello')
def hello():
    time.sleep(10)
    return 'Hello!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)
