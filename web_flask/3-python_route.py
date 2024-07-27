#!/usr/bin/python3
"""This module defines a flask instance """
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Function to be called on the route /"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """function to be called on the /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def HBNB_text(text):
    """displaying variable rules"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def HBNB_python(text='cool'):
    """displaying variable rules with optional default value"""
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
