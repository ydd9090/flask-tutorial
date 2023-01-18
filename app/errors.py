from flask import render_template
from app import app
from app.models import User


@app.errorhandler(404)
def page_not_found(e):
    user = User.query.first()
    return render_template("404.html",user=user),404
