from flask import Flask
import os 
import socket


app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello World!"


@app.route("/hello")
def hello_page():
    html="<h2>Welcome to Docker & Python based WebServer<\h2>"\
         "<b>Hostname: {hostname}</b>"
    return html.format(hostname=socket.gethostname())

app.run('0.0.0.0',80)
