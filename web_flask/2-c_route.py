#!/usr/bin/python3
"""
A script that starts a Flask application:
Listening on 0.0.0.0:5000
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """"displays: Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays: HBNB"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """displays: C followed by the value
        of the text variable"""
    return "C %s" % text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
