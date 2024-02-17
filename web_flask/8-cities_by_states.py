#!/usr/bin/python3
""" Flask app to list state local cities """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Routes cities by states page"""

    states = storage.all(State).values()

    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def session_scope(exception):
    """ Ends a storage session starting another"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
