#!/usr/bin/python3
""" Script that starts a Flask web application
"""
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ return given text"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return a given text """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """Display "C" followed by text """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    """ Display Python followed by text """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    """ return is the n is number """
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=None)
