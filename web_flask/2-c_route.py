#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Display Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display HBNB!"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text_c(text):
    """C<Text>"""
    new_text = text.replace("_", " ")
    return "C {}".format(new_text)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
