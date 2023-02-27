from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,validators,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,InputRequired,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('username',
                    validators=[DataRequired(),Length(min=2,max=20)])
    email = EmailField("Email",  validators=[InputRequired("Please enter your email address.")]), validators.Email("Please enter your email address.")
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign_up')


class LoginForm(FlaskForm):
    email = EmailField("Email",  validators=[InputRequired("Please enter your email address.")]), validators.Email("Please enter your email address.")
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember_me')
    submit = SubmitField('Log_in')    