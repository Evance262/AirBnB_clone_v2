#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes=False


@app.route('/')
def hello_route():
    """Program that starts a Flask web application"""
    return 'Hello HBNB!'