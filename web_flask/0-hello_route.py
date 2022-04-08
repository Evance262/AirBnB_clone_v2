#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    """Program that starts a Flask web application"""
    return 'Hello HBNB!'
