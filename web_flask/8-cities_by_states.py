#!/usr/bin/python3
"""Script that starts a Flask web application"""
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.teardown_appcontext
def close(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    List of all State and City objects present in DBStorage sorted by name (A->Z)
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states_key=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
