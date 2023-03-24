from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    """ Returns welcome greeting."""
    msg = "<h1>Welcome</h1>"
    return msg


@app.route('/welcome/home')
def say_welcomehome():
    """ Returns welcome home greeting."""
    msg = "<h1>Welcome home</h1>"
    return msg

@app.route('/welcome/back')
def say_welcomeback():
    """ Returns welcome back greeting."""
    msg = "<h1>Welcome back</h1>"
    return msg