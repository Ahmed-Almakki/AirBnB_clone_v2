#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ hello function first page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ seconde page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def texxt(text):
    strg = ''
    for i in text:
        if i == '_':
            strg += ' '
        else:
            strg += i
    return "C " + strg


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyth_text(text):
    t = ""
    for i in text:
        if i == '_':
            t += ' '
        else:
            t += i
    return "Python " + t


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
