from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email,EqualTo, ValidationError
from minorproj.models import User
import pandas as pd

filename = pd.read_csv('F:\\web development\\Minor Project\\cities.csv')
df = filename['name_of_city']

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken!')
    
    def validate_email(self, email):
       user = User.query.filter_by(email=email.data).first()
       if user:
           raise ValidationError('email is taken!')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class dropdown(FlaskForm):
    select = SelectField('Chose a City',choices=[(f,f) for f in df])
    submit = SubmitField('Add')
