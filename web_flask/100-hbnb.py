#/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.place import Place
from models.amenity import Amenity
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display the hbnb stactic page
    """
    all_data_place = storage.all("Place")
    all_data_state = storage.all("State")
    all_data_amenity = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", states_key=all_data_state,
                                        amenities_key=all_data_amenity,
                                        places_key=all_data_place)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
