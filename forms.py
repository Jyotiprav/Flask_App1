from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class addinfo(FlaskForm):
    username=StringField('Username')
    password = PasswordField('Password')
    email=StringField('Email')
    phoneno=StringField('Phone Number')
    submit = SubmitField('Add')