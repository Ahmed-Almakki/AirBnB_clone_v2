#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask


app = Flask(__name__)
app.config['SERVER_NAME'] = '0.0.0.0:5000'


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


app.run()
