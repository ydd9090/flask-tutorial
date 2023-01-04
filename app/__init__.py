from markupsafe import escape

from flask import Flask


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello_world():
    return "<div><center><h1>Hello World!</h1></center></div>"

@app.route("/hello")
def hello_totoro():
    return '<center><h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif"></center>'

@app.route("/user/<name>")
def user_page(name):
    return f"User: {escape(name)}"
