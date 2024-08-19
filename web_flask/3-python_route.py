#!/usr/bin/python3

"""Starts a Flask web application.

This script sets up a basic Flask web application,
 that listens on 0.0.0.0, port 5000,
and displays the message 'Hello HBNB!' when the root URL is accessed.

Usage:
    Run this script directly to start the Flask application.

Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable

Return:
    None
"""

from flask import Flask
from markupsafe import escape
# escape ensure that any user-provided data is safely handled by
# escaping characters
# that could be interpreted as HTML or JavaScript.


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Displays 'Hello HBNB!' at the root URL."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns 'HBNB' on the /hbnb route."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """"
    Displays 'C' followed by the value of 'text',
      replacing underscores with spaces.
    """
    new_text = ''
    for char in text:
        if char == '_':
            new_text += ' '
        else:
            new_text += char
    return f'C {escape(new_text)}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """"
    Displays 'Python' followed by the value of 'text',
    replacing underscores with spaces. Defaults to 'is cool'.
    """
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
