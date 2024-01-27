#!/usr/bin/python3
"""
Module with script that starts a flask web project
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ """
    return "C {}".format(text)


if __name__ == '__main__':
    """ """
    app.run(host='0.0.0.0', port=5000)