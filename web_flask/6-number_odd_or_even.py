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

from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if 'n' is an integer."""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """
    Displays a HTML page with 'Number: n is even' or 'Number: n is odd'
    inside an H1 tag based on whether 'n' is even or odd.
    """
    result = 'odd' if n % 2 else 'even'
    return render_template('6-number_odd_or_even.html', n=n, parity=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
