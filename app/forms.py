from flask_wtf import FlaskForm 
from wtforms import StringField, BooleanField, PasswordField, IntegerField, SelectField, DateTimeField, DateField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo

class LoginForm(FlaskForm):
    id = IntegerField('User ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class SignUpForm(FlaskForm):
    id = IntegerField('Choose ID (3 Numbers)', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), 
                                                     Length(min=6, message='Password should be at least 6 characters long')])
    password2 = PasswordField('Password Confirmation', validators=[DataRequired(), 
                                                                   Length(min=6, message='Password should be at least 6 characters long'), 
                                                                   EqualTo('password', message="Password must match")])