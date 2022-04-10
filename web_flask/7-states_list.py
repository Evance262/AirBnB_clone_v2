#!/usr/bin/python3
"""
A script that starts a Flask application:
Listening on 0.0.0.0:5000
"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """displays: states list"""
    all_states = storage.all(State)
    return render_template('7-states_list.html', states=all_states)


@app.teardown_appcontext
def teardown_appcontext(self):
    """remove the current SQLAlchemy Session"""
    return storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
