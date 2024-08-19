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

Return:
    None
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Displays 'Hello HBNB!' at the root URL."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns 'HBNB' on the /hbnb route."""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
