from google.appengine.ext import ndb
from google.cloud import datastore, storage
from wtforms import *
from wtforms.validators import *


class User(ndb.Model):
    id = datastore.Entity.id


class LoginForm(Form):
    loginID = StringField('Login ID: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')


# class RegisterForm(Form):

def init_users():
    client = datastore.Client()
    user0 = datastore.Entity(client.key('user'))
    user0.update({
        'id': 's39109020',
        'password': '012345',
        'user_name': 'Arian Najafi Yamchelo0',
        'user_profile_img': 'zero.jpg'
    })

    user1 = datastore.Entity(client.key('user'))
    user1.update({
        'id': 's39109021',
        'password': '123456',
        'user_name': 'Arian Najafi Yamchelo1',
        'user_profile_img': 'one.jpg'
    })

    user2 = datastore.Entity(client.key('user'))
    user2.update({
        'id': 's39109022',
        'password': '234567',
        'user_name': 'Arian Najafi Yamchelo2',
        'user_profile_img': 'two.jpg'

    })

    user3 = datastore.Entity(client.key('user'))
    user3.update({
        'id': 's39109023',
        'password': '345678',
        'user_name': 'Arian Najafi Yamchelo3',
        'user_profile_img': 'three.jpg'
    })

    user4 = datastore.Entity(client.key('user'))
    user4.update({
        'id': 's39109024',
        'password': '456789',
        'user_name': 'Arian Najafi Yamchelo4',
        'user_profile_img': 'four.jpg'
    })

    user5 = datastore.Entity(client.key('user'))
    user5.update({
        'id': 's39109025',
        'password': '567890',
        'user_name': 'Arian Najafi Yamchelo5',
        'user_profile_img': 'five.jpg'
    })

    user6 = datastore.Entity(client.key('user'))
    user6.update({
        'id': 's39109026',
        'password': '678901',
        'user_name': 'Arian Najafi Yamchelo6',
        'user_profile_img': 'six.jpg'
    })

    user7 = datastore.Entity(client.key('user'))
    user7.update({
        'id': 's39109027',
        'password': '789012',
        'user_name': 'Arian Najafi Yamchelo7',
        'user_profile_img': 'seven.jpg'
    })

    user8 = datastore.Entity(client.key('user'))
    user8.update({
        'id': 's39109028',
        'password': '890123',
        'user_name': 'Arian Najafi Yamchelo8',
        'user_profile_img': 'eight.jpg'
    })

    user9 = datastore.Entity(client.key('user'))
    user9.update({
        'id': 's39109029',
        'password': '901234',
        'user_name': 'Arian Najafi Yamchelo9',
        'user_profile_img': 'nine.jpg'
    })

    client.put_multi([user0, user1, user2, user3, user4, user5, user6, user7, user8, user9])
