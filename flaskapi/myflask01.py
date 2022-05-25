#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask #capital F means flask is a Class we are importing

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)#app means the whole application, we are goingto teach app what to do
                     #from the main script

#clients send a GET request to our home page
#they will receive back the return statement "Hello World"

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/")
def hello_world():
   return "Hello World"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE

