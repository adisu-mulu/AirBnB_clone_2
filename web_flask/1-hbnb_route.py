#!/usr/bin/python3
"""This module defines a flask instance """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Function to be called on the route /"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
