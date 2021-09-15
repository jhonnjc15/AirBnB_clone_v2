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


@app.route('/states', strict_slashes=False)
def states_list():
    """
    List of all State objects present in DBStorage sorted by name (A->Z)
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states_key=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """
    List the states by id ir order
    """
    all_data = storage.all("State").values()
    state = {}
    for data in all_data:
        if data.id == id:
            state = data
            break
        else:
            state = None
    return render_template("9-states.html", state_key=state)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
