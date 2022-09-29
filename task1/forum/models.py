import pytz
import datetime
import tzlocal as tzlocal
from flask_wtf import FlaskForm
from google.cloud import ndb, storage
from wtforms.validators import InputRequired
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField

storage_client = storage.Client.from_service_account_json(
    json_credentials_path='task1/cc-a1-task1.json')

# storage_client = storage.Client()


class Post(ndb.Model):
    subject = ndb.StringProperty()
    message_text = ndb.StringProperty()
    user_post_img = ndb.StringProperty()
    date_and_time = ndb.DateTimeProperty()


class User(ndb.Model):
    login_id = ndb.StringProperty()
    password = ndb.StringProperty()
    user_name = ndb.StringProperty()
    user_profile_img = ndb.StringProperty()
    posts = ndb.StructuredProperty(Post, indexed=True, repeated=True)


class LoginForm(FlaskForm):
    login_id = StringField('ID', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    login_id = StringField('ID', validators=[InputRequired()])
    user_name = StringField('User name', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    user_profile_img = FileField('Profile image')
    submit = SubmitField('Register')


class EditPasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[InputRequired()])
    new_password = PasswordField('New password', validators=[InputRequired()])
    submit = SubmitField('Change')


class CreatePostForm(FlaskForm):
    subject = StringField('Subject', validators=[InputRequired()])
    message_text = TextAreaField('Message')
    user_post_img = FileField('Add image')
    submit = SubmitField('Create')


class EditPostForm(FlaskForm):
    subject = StringField('Subject', validators=[InputRequired()])
    message_text = TextAreaField('Message')
    user_post_img = FileField('Update image')
    submit = SubmitField('Update')


def upload_profile_img(user_profile_img, login_id, filename):
    bucket = storage_client.bucket('forum_image_bucket')
    blob = bucket.blob(login_id + "_" + filename)
    blob.upload_from_file(user_profile_img, content_type='image/jpeg')


def upload_post_img(user_post_img, login_id, post_date_and_time, filename):
    bucket = storage_client.bucket('forum_image_bucket')
    blob = bucket.blob(login_id + "_" + post_date_and_time + "_" + filename)
    blob.upload_from_file(user_post_img, content_type='image/jpeg')


def generate_url(blob_name):
    bucket = storage_client.bucket('forum_image_bucket')
    blob = bucket.blob(blob_name)
    return blob.generate_signed_url(method='GET', expiration=datetime.timedelta(minutes=60))


def convert_utc_to_local_time(date_and_time):
    local_date_and_time = date_and_time.replace(tzinfo=pytz.utc).astimezone(tzlocal.get_localzone())
    formatted_date_and_time = local_date_and_time.strftime('%d/%m/%Y %H:%M')
    return formatted_date_and_time


def init_users():
    user0 = User(login_id='s39109020', password='012345', user_name='Arian Najafi Yamchelo0',
                 user_profile_img='s39109020_zero.jpg', id='s39109020')
    user1 = User(login_id='s39109021', password='123456', user_name='Arian Najafi Yamchelo1',
                 user_profile_img='s39109021_one.jpg', id='s39109021')
    user2 = User(login_id='s39109022', password='234567', user_name='Arian Najafi Yamchelo2',
                 user_profile_img='s39109022_two.jpg', id='s39109022')
    user3 = User(login_id='s39109023', password='345678', user_name='Arian Najafi Yamchelo3',
                 user_profile_img='s39109023_three.jpg', id='s39109023')
    user4 = User(login_id='s39109024', password='456789', user_name='Arian Najafi Yamchelo4',
                 user_profile_img='s39109024_four.jpg', id='s39109024')
    user5 = User(login_id='s39109025', password='567890', user_name='Arian Najafi Yamchelo5',
                 user_profile_img='s39109025_five.jpg', id='s39109025')
    user6 = User(login_id='s39109026', password='678901', user_name='Arian Najafi Yamchelo6',
                 user_profile_img='s39109026_six.jpg', id='s39109026')
    user7 = User(login_id='s39109027', password='789012', user_name='Arian Najafi Yamchelo7',
                 user_profile_img='s39109027_seven.jpg', id='s39109027')
    user8 = User(login_id='s39109028', password='890123', user_name='Arian Najafi Yamchelo8',
                 user_profile_img='s39109028_eight.jpg', id='s39109028')
    user9 = User(login_id='s39109029', password='901234', user_name='Arian Najafi Yamchelo9',
                 user_profile_img='s39109029_nine.jpg', id='s39109029')

    ndb.put_multi([user0, user1, user2, user3, user4, user5, user6, user7, user8, user9])
