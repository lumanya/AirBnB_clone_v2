#!/usr/bin/python3
""" script that starts web application and make application
listening on 0.0.0.0 and port 5000
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ return given string """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return a given string """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
