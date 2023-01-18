import os
from markupsafe import escape

from flask import render_template,redirect,url_for,flash,send_from_directory,request
from flask_login import login_user,login_required,logout_user

from app import app,db
from app.models import User,Movie
from app.forms import EditForm,LoginForm,SearchForm


@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.first()
        if user.username == username and user.validate_password(password):
            login_user(user,form.remember.data)
            flash("登录成功")
            return redirect(url_for('index'))
        
        flash("登录失败，密码或用户名不正确")
        return redirect(url_for('login'))
    return render_template("login.html",form=form)

@app.route("/logout",methods=["GET","POST"])
@login_required
def logout():
    logout_user()
    flash("登出成功")
    return redirect(url_for("index"))

@app.route("/",methods=["GET","POST"])
def index():
    form = EditForm()
    if form.validate_on_submit():
        title = form.title.data
        year = form.year.data
        if Movie.query.filter(Movie.title==title,Movie.year==year).first():
            flash("该电影已存在")
            return redirect(url_for('index'))
        movie = Movie(title=title,year=year)
        db.session.add(movie)
        db.session.commit()
    # movies = Movie.query.all()
    page = request.args.get("page",1,type=int)
    pagination = Movie.query.order_by(Movie.year.desc()).paginate(page=page,per_page=5)
    movies_count = Movie.query.count()
    movies = pagination.items
    return render_template("index.html",movies_count=movies_count,movies=movies,form=form,pagination=pagination)

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

@app.route("/edit/<int:movie_id>",methods=["GET","POST"])
@login_required
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    form = EditForm()

    if form.validate_on_submit():
        title = form.title.data
        year = form.year.data
        app.logger.info("edit new title:{},edit new year:{}".format(title,year))
        movie.title = title
        movie.year = year
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        flash("回填数据，done","debug")
        form.title.data = movie.title
        form.year.data = movie.year
    return render_template("edit.html",form=form)

@app.route("/delete/<int:movie_id>",methods=["POST"])
@login_required
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash("删除成功！")
    return redirect(url_for("index"))

@app.route("/search",methods=["GET","POST"])
def search():
    
    form = SearchForm()

    if form.validate_on_submit():
        flash("该功能还在开发中，敬请期待～")
        return redirect(url_for('search'))
    return render_template("search.html",form=form)



@app.route("/avatars/<path:filename>")
def get_avatar(filename):
    return send_from_directory(app.config["AVATARS_SAVE_PATH"],filename)