#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def close(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    List the states by id ir order
    """
    all_data_state = storage.all("State")
    all_data_amenity = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", states_key=all_data_state,
                                        amenities_key=all_data_amenity)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
