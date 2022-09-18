from wtforms import *
from wtforms.validators import *


class LoginForm(Form):
    loginID = StringField('Login ID: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')

# class RegisterForm(Form):
