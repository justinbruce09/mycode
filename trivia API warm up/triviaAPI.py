#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/")
def triviaQuestion():
    return "I am always around, but when you say my name I disappear"

@app.route("/correct")
def correctAnswer():
    return "correct"

@app.route("/checkanswer", methods = ["POST"])
def checkanswer(answer):
    if answer == "silence":
        return redirect(url_for("correctAnswer"))
    else:
        return redirect(url_for("triviaQuestion"))

