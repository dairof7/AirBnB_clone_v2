#!/usr/bin/python3
"""Start a Flask web application"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """function to execute"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello2():
    """function to execute"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def string(text):
    """function to execute"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def string2(text='is cool'):
    """function to execute when use get"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
