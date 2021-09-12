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


@app.route('/states_list', strict_slashes=False)
def display_states_list():
    """ Function that displays a HTML page """
    dict = storage.all(State)
    return render_template('7-states_list.html', dict=dict)


if __name__ == '__main__':
    app.run(debug=True, port='5000', host='0.0.0.0')
