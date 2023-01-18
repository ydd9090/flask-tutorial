import click
from app import app,db
from app.models import User,Movie


@app.cli.command()
@click.option("--drop",is_flag=True,help="是否先删除已存在的数据库")
@click.option("--with-admin",is_flag=True,)
def initdb(drop,with_admin):
    if drop:
        click.confirm("确认先删除已存在的数据库？",abort=True)
        db.drop_all()
    if with_admin:
        click.echo("创建admin用户")
        pass
    db.create_all()
    # user = User(username="Tobey",name="Tobey")
    # db.session.add(user)
    # db.session.commit()
    click.echo("初始化数据库成功！")


@app.cli.command()
def forge():
    db.create_all()

    name = "Tobey"
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
    user = User(name=name,username="admin")
    user.set_password("admin")
    db.session.add(user)
    db.session.commit()
    user = User.query.first()
    for m in movies:
        movie = Movie(title=m["title"],year=m["year"],user_id = user.id)
        db.session.add(movie)
    db.session.commit()
    click.echo("done.")


@app.cli.command()
@click.option("--username",prompt=True,help="管理员用户名")
@click.option("--password",prompt=True,hide_input=True,confirmation_prompt=True,help="管理员密码")
def admin(username,password):
    db.create_all()

    user = User.query.first()
    if user is not None:
        click.echo("更新用户")
        user.username = username
        user.set_password(password)
    else:
        click.echo("创建用户")
        user = User(username=username,name="Admin")
        user.set_password(password)
        db.session.add(user)
    db.session.commit()
    click.echo("完成")

