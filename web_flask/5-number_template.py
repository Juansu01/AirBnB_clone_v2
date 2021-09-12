#!/usr/bin/python3
"""This module sets up a flask server"""
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')


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


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """This function retunrs a string saying HBNB"""
    replace = text.replace("_", " ")
    return "Python {}".format(replace)


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """This function retunrs a number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_me_the_int(n):
    """ Returns a page with integer if n is type int """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run()
