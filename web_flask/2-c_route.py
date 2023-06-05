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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=None)
