#!/usr/bin/python3
"""This module sets up a flask server"""
from flask import Flask
app = Flask('')


@app.route('/', strict_slashes=False)
def index():
    """This function retunrs a string saying Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def meow():
    """This function retunrs a string saying HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """This function retunrs a string saying HBNB"""
    replace = text.replace("_", " ")
    my_string = "C {}".format(replace)
    return my_string


@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """This function retunrs a string saying HBNB"""
    if text:
        replace = text.replace("_", " ")
        my_string = "Python {}".format(replace)
        return my_string
    else:
        return "Python is cool"


if __name__ == '__main__':
    app.run()
