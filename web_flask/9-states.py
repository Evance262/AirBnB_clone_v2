#!/usr/bin/python3
''' Flask web application '''

from flask import Flask
from flask import render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state(id=None):
    """Displays states list"""
    if id is not None:
        id = 'State.' + id

    all_states = storage.all(State)
    return render_template('9-states.html', states=all_states, s_id=id)


@app.teardown_appcontext
def teardown_appcontext(self):
    """Remove the current SQLAlchemy Session"""
    return storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
