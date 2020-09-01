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


@app.route('/states_list', strict_slashes=False)
def stateList():
    """function to execute"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
