#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
from flask import render_template


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
    """Display C<Text>"""
    new_text = text.replace("_", " ")
    return "C {}".format(new_text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_python(text='is cool'):
    """Display Python<text>"""
    new_text = text.replace("_", " ")
    return "Python {}".format(new_text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """Display a number, if this number is integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_number_n(n):
    """Display a number, if this number is integer"""
    return render_template('5-number.html', n_key=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
