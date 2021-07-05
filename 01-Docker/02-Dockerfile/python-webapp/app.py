from flask import Flask
import os 
import socket


app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello World!"


app.run('0.0.0.0',80)
