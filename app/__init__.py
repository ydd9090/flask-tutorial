from markupsafe import escape

from flask import Flask,render_template


name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",name=name,movies=movies)

@app.route("/index")
@app.route("/home")
def hello_world():
    return "<div><center><h1>Hello World!</h1></center></div>"

@app.route("/hello")
def hello_totoro():
    return '<center><h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif"></center>'

@app.route("/user/<name>")
def user_page(name):
    return f"User: {escape(name)}"
