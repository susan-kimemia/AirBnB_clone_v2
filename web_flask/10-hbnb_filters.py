#!/usr/bin/python3

""" Web app for hbnb content """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters')
def hbnb_filters():
    """
    Displays hbnb filters page
    """

    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def tear_down(exception):
    """Cleans session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
