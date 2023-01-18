from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Length


class EditForm(FlaskForm):
    title  = StringField(label="电影名",validators=[DataRequired()])
    year   = IntegerField(label="上映年份",validators=[DataRequired()])
    submit = SubmitField(label="提交")

class LoginForm(FlaskForm):
    username = StringField("用户名",validators=[DataRequired()])
    password = PasswordField("密码",validators=[DataRequired()])
    remember = BooleanField("记住我")
    submit   = SubmitField("登录")


class SearchForm(FlaskForm):
    keyword = StringField("关键字",validators=[DataRequired(),Length(1,60)])
    submit  = SubmitField("搜索")