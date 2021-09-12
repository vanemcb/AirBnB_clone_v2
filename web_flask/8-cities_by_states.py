#!/usr/bin/python3
""" script that starts a Flask web application """

from models.state import State
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """ Function that removes the current SQLAlchemy Session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_by_states():
    """ Function that displays a HTML page """
    dict = storage.all(State)
    return render_template('8-cities_by_states.html', dict=dict)


if __name__ == '__main__':
    app.run(debug=True, port='5000', host='0.0.0.0')
