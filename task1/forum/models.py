from google.cloud import ndb
from wtforms import *
from wtforms.validators import *


class User(ndb.Model):
    id = ndb.StringProperty()
    password = ndb.StringProperty()
    user_name = ndb.StringProperty()
    user_profile_img = ndb.StringProperty()


class LoginForm(Form):
    loginID = StringField('Login ID: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')


# class RegisterForm(Form):

def init_users():

    user0 = User(id='s39109020', password='012345', user_name='Arian Najafi Yamchelo0',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/zero.jpg')
    user1 = User(id='s39109021', password='123456', user_name='Arian Najafi Yamchelo1',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/one.jpg')
    user2 = User(id='s39109022', password='234567', user_name='Arian Najafi Yamchelo2',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/two.jpg')
    user3 = User(id='s39109023', password='345678', user_name='Arian Najafi Yamchelo3',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/three.jpg')
    user4 = User(id='s39109024', password='456789', user_name='Arian Najafi Yamchelo4',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/four.jpg')
    user5 = User(id='s39109025', password='567890', user_name='Arian Najafi Yamchelo5',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/five.jpg')
    user6 = User(id='s39109026', password='678901', user_name='Arian Najafi Yamchelo6',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/six.jpg')
    user7 = User(id='s39109027', password='789012', user_name='Arian Najafi Yamchelo7',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/seven.jpg')
    user8 = User(id='s39109028', password='890123', user_name='Arian Najafi Yamchelo8',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/eight.jpg')
    user9 = User(id='s39109029', password='901234', user_name='Arian Najafi Yamchelo9',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/nine.jpg')

    ndb.put_multi([user0, user1, user2, user3, user4, user5, user6, user7, user8, user9])
