#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/correct")
def success():
    return f"That is correct!"

@app.route("/<username>")   # to pass username into the function, maybe add it to the route /<username>
def start(username):
    return render_template("trivia2.html", name=username)

@app.route("/login", methods = ["POST"])
def login():
        if request.form.get("nm") and request.form.get("nm") == "42":
                return redirect("/correct")
        else:
            return redirect("/")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
