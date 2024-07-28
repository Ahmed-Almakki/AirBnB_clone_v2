#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template


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


@app.route("/number/<int:n>", strict_slashes=False)
def nmbr(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def url_buld(n):
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_odd(n):
    if n % 2 == 0:
        tx = "is even"
    else:
        tx = "is odd"
    return render_template('6-number_odd_or_even.html', n=n, tx=tx)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
