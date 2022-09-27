from flask_wtf import FlaskForm
from google.cloud import ndb
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import InputRequired


class Post(ndb.Model):
    subject = ndb.StringProperty()
    content = ndb.StringProperty()
    image = ndb.StringProperty()


class User(ndb.Model):
    login_id = ndb.StringProperty()
    password = ndb.StringProperty()
    user_name = ndb.StringProperty()
    user_profile_img = ndb.StringProperty()
    posts = ndb.StructuredProperty(Post, repeated=True)


class LoginForm(FlaskForm):
    login_id = StringField('ID', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    login_id = StringField('ID', validators=[InputRequired()])
    user_name = StringField('User name', validators=[InputRequired()])
    password = StringField('Password', validators=[InputRequired()])
    user_profile_img = FileField('Profile image')
    submit = SubmitField('Register')


def init_users():
    user0 = User(login_id='s39109020', password='012345', user_name='Arian Najafi Yamchelo0',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/zero.jpg', id='s39109020')
    user1 = User(login_id='s39109021', password='123456', user_name='Arian Najafi Yamchelo1',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/one.jpg', id='s39109021')
    user2 = User(login_id='s39109022', password='234567', user_name='Arian Najafi Yamchelo2',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/two.jpg', id='s39109022')
    user3 = User(login_id='s39109023', password='345678', user_name='Arian Najafi Yamchelo3',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/three.jpg', id='s39109023')
    user4 = User(login_id='s39109024', password='456789', user_name='Arian Najafi Yamchelo4',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/four.jpg', id='s39109024')
    user5 = User(login_id='s39109025', password='567890', user_name='Arian Najafi Yamchelo5',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/five.jpg', id='s39109025')
    user6 = User(login_id='s39109026', password='678901', user_name='Arian Najafi Yamchelo6',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/six.jpg', id='s39109026')
    user7 = User(login_id='s39109027', password='789012', user_name='Arian Najafi Yamchelo7',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/seven.jpg', id='s39109027')
    user8 = User(login_id='s39109028', password='890123', user_name='Arian Najafi Yamchelo8',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/eight.jpg', id='s39109028')
    user9 = User(login_id='s39109029', password='901234', user_name='Arian Najafi Yamchelo9',
                 user_profile_img='gs://forum_user_profile_img/user_profile_img/nine.jpg', id='s39109029')

    ndb.put_multi([user0, user1, user2, user3, user4, user5, user6, user7, user8, user9])
