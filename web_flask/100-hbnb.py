#!/usr/bin/python3
"""Starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.place import Place
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """Close session - teardown storage"""

    storage.close()


@app.route('/hbnb', strict_slashes=False)
def filters_action(id=None):
    """filters"""

    return render_template(
        '100-hbnb.html',
        states=storage.all(State).values(),
        amenities=storage.all(Amenity).values(),
        places=storage.all(Place).values()
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
