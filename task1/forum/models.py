import pytz
import datetime
import tzlocal as tzlocal
from flask_wtf import FlaskForm
from google.cloud import ndb, storage
from wtforms.validators import InputRequired
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField

# storage_client = storage.Client.from_service_account_json(
#     json_credentials_path='task1/cc-a1-task1.json')

storage_client = storage.Client()


# Code sourced and adapted from:

# [8] "flask form", pythonspot, 2022. [Online]. Available: https://pythonspot.com/flask-web-forms/. [Accessed: 29-
# Sep- 2022].

# [9] M. Grinberg, "Handling File Uploads With Flask", Blog.miguelgrinberg.com, 2022. [Online]. Available:
# https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask. [Accessed: 29- Sep- 2022].
#
# [10] "Ideal Flask project structure for absolutely scalable web application in 2021 - Coders Diaries",
# Codersdiaries.com, 2022. [Online]. Available: https://www.codersdiaries.com/blog/flask-project-structure. [
# Accessed: 29- Sep- 2022].
#
# [11] creativecreatorormaybenot and vishes_shell, "ModuleNotFoundError: No module named 'models'", Stack Overflow,
# 2022. [Online]. Available: https://stackoverflow.com/questions/45020963/modulenotfounderror-no-module-named-models.
# [Accessed: 29- Sep- 2022].

# [12] "Entities, Properties, and Keys  |  Cloud Datastore Documentation  |  Google Cloud", Google Cloud,
# 2022. [Online]. Available: https://cloud.google.com/datastore/docs/concepts/entities#datastore-datastore-lookup
# -python. [Accessed: 29- Sep- 2022].
#
# [13] "Entities, Properties, and Keys  |  Cloud Datastore Documentation  |  Google Cloud", Google Cloud,
# 2022. [Online]. Available: https://cloud.google.com/datastore/docs/concepts/entities#datastore-datastore-update
# -python. [Accessed: 29- Sep- 2022].
#
# [14] "Download objects  |  Cloud Storage  |  Google Cloud", Google Cloud, 2022. [Online]. Available:
# https://cloud.google.com/storage/docs/downloading-objects#prereq-code-samples. [Accessed: 29- Sep- 2022].
#
# [15] "NDB Model Class  |  App Engine standard environment for Python 2  |  Google Cloud", Google Cloud,
# 2022. [Online]. Available: https://cloud.google.com/appengine/docs/legacy/standard/python/ndb/modelclass. [
# Accessed: 29- Sep- 2022].
#
# [16] "Entities, Properties, and Keys  |  App Engine standard environment for Python 2  |  Google Cloud",
# Google Cloud, 2022. [Online]. Available: https://cloud.google.com/appengine/docs/legacy/standard/python/datastore
# /entities. [Accessed: 29- Sep- 2022].
#
# [17] "Polymorphic Models and Queries — ndb documentation", Googleapis.dev, 2022. [Online]. Available:
# https://googleapis.dev/python/python-ndb/latest/polymodel.html. [Accessed: 29- Sep- 2022].
#
# [18] "Cloud NDB: `ImportError: No module named cloud.` · Issue #518 · googleapis/python-ndb", GitHub,
# 2022. [Online]. Available: https://github.com/googleapis/python-ndb/issues/518. [Accessed: 29- Sep- 2022].
#
# [19] "ndb library for Google Cloud Datastore — ndb documentation", Googleapis.dev, 2022. [Online]. Available:
# https://googleapis.dev/python/python-ndb/latest/index.html. [Accessed: 29- Sep- 2022].
#
# [20] C. Rossi, "Python NDB Library Issue · Issue #568 · googleapis/python-ndb", GitHub, 2022. [Online]. Available:
# https://github.com/googleapis/python-ndb/issues/568. [Accessed: 29- Sep- 2022].
#
# [21] r. moraes, "NDB Cheat Sheet", Docs.google.com, 2022. [Online]. Available:
# https://docs.google.com/document/d/1AefylbadN456_Z7BZOpZEXDq8cR8LYu7QgI7bt5V0Iw/mobilebasic. [Accessed: 29- Sep-
# 2022].
#
# [22] VizslaVizsla and O. Kanji, "How to upload an image using WTF forms quick form", Stack Overflow,
# 2022. [Online]. Available: https://stackoverflow.com/questions/50168932/how-to-upload-an-image-using-wtf-forms
# -quick-form. [Accessed: 29- Sep- 2022].

# [26] "Migrating to Cloud NDB  |  App Engine standard environment for Python 3  |  Google Cloud", Google Cloud,
# 2022. [Online]. Available: https://cloud.google.com/appengine/docs/standard/python3/migrating-to-cloud-ndb. [
# Accessed: 29- Sep- 2022].

# [42] M. Nascimento and J. Hanley, "Unable to assign iam.serviceAccounts.signBlob permission", Stack Overflow,
# 2022. [Online]. Available: https://stackoverflow.com/questions/57564505/unable-to-assign-iam-serviceaccounts
# -signblob-permission. [Accessed: 29- Sep- 2022].

# [44] "Bootstrap Vertical alignment - examples & tutorial", MDB - Material Design for Bootstrap, 2022. [Online].
# Available: https://mdbootstrap.com/docs/standard/layout/vertical-alignment/. [Accessed: 29- Sep- 2022].
#
# [45] h. Alexej, "list of pytz time zones", Gist, 2022. [Online]. Available:
# https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568. [Accessed: 29- Sep- 2022].
#
# [46] L. Stanley, R. Cowie, Никита Шишкин and gerardw, "Call a python function from jinja2", Stack Overflow,
# 2022. [Online]. Available: https://stackoverflow.com/questions/6036082/call-a-python-function-from-jinja2. [
# Accessed: 29- Sep- 2022].
#
# [47] "NDB Queries  |  App Engine standard environment for Python 2  |  Google Cloud", Google Cloud, 2022. [Online].
# Available: https://cloud.google.com/appengine/docs/legacy/standard/python/ndb/queries. [Accessed: 29- Sep- 2022].
#
# [48] J. Holloway, D. Foster, M. Tolonen and jfs, "Convert UTC datetime string to local datetime", Stack Overflow,
# 2022. [Online]. Available: https://stackoverflow.com/questions/4770297/convert-utc-datetime-string-to-local
# -datetime. [Accessed: 29- Sep- 2022].
#
# [49] R. Vuta, "How to change the format of date in Python", codespeedy, 2022. [Online]. Available:
# https://www.codespeedy.com/change-the-format-of-date-in-python/. [Accessed: 29- Sep- 2022].
#
# [50] "Aligning items in a flex container - CSS&colon; Cascading Style Sheets | MDN", Developer.mozilla.org,
# 2022. [Online]. Available: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout
# /Aligning_Items_in_a_Flex_Container. [Accessed: 29- Sep- 2022].
#
# [51] J. Moran, Zim, Giacomo1968 and mahan, "Bootstrap 4 Flexbox force rows to fill vertical space inside col",
# Stack Overflow, 2022. [Online]. Available: https://stackoverflow.com/questions/50144411/bootstrap-4-flexbox-force
# -rows-to-fill-vertical-space-inside-col. [Accessed: 29- Sep- 2022].
#
# [52] R. Gurung, E. Popal and davidism, "Passing variables through URL to a flask app", Stack Overflow,
# 2022. [Online]. Available: https://stackoverflow.com/questions/24052362/passing-variables-through-url-to-a-flask
# -app. [Accessed: 29- Sep- 2022].


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
