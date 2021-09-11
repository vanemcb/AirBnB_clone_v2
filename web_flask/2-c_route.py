#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display():
    """ Function that displays “Hello HBNB!” """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Function that displays “HBNB” """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """ Function that displays “C” followed by the value of
    the text variable """
    return 'C {}'.format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(debug=True, port='5000', host='0.0.0.0')