#!/usr/bin/python3
"""Start a Flask web application"""


from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_db(self):
    """Close session"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def stateList(id=None):
    """function to execute"""
    states = storage.all(State)
    id_state = None
    state = None
    if id:
        id_state = 'State.' + id
        if id_state in states.keys():
            state = states[id_state]
    return render_template('9-states.html', id=id_state,
                           state=state, states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
