from flask import render_template, flash, Blueprint, redirect, session, request
from werkzeug.utils import secure_filename
from .models import *
from google.cloud import ndb

forum = Blueprint('forum', __name__, template_folder="templates/forum")
client = ndb.Client()


# Code sourced and adapted from:

# [4] R. Simon, "Flask application with multiple views, how does 'flask run' work in this case?", Stack Overflow,
# 2022. [Online]. Available: https://stackoverflow.com/questions/49734284/flask-application-with-multiple-views-how
# -does-flask-run-work-in-this-case. [Accessed: 29- Sep- 2022].
#
# [5] "Large Applications as Packages — Flask Documentation (2.0.x)", Flask.palletsprojects.com, 2022. [Online].
# Available: https://flask.palletsprojects.com/en/2.0.x/patterns/packages/. [Accessed: 29- Sep- 2022].
#
# [6] "Project Layout — Flask Documentation (2.1.x)", Flask.palletsprojects.com, 2022. [Online]. Available:
# https://flask.palletsprojects.com/en/2.1.x/tutorial/layout/. [Accessed: 29- Sep- 2022].
#
# [7] Harrison, "Python Programming Tutorials", Pythonprogramming.net, 2022. [Online]. Available:
# https://pythonprogramming.net/flask-registration-tutorial/?completed=/flask-user-registration-form-tutorial/. [
# Accessed: 29- Sep- 2022].

# [23] D. Robinson, Z. Maret and T. Orozco, "TypeError: __init__() takes 0 positional arguments but 1 was given",
# Stack Overflow, 2022. [Online]. Available:
# https://stackoverflow.com/questions/25902690/typeerror-init-takes-0-positional-arguments-but-1-was-given. [
# Accessed: 29- Sep- 2022].
#
# [24] tynn, "Python: How to import from an __init__.py file?", Stack Overflow, 2022. [Online]. Available:
# https://stackoverflow.com/questions/22282316/python-how-to-import-from-an-init-py-file. [Accessed: 29- Sep- 2022].
#
# [25] D. Smith, "FlaskForm not Validating on Submit", Stack Overflow, 2022. [Online]. Available:
# https://stackoverflow.com/questions/64451987/flaskform-not-validating-on-submit. [Accessed: 29- Sep- 2022].

# [27] yameenvinchu, "How to use Flask-Session in Python Flask ? - GeeksforGeeks", GeeksforGeeks, 2022. [Online].
# Available: https://www.geeksforgeeks.org/how-to-use-flask-session-in-python-flask/. [Accessed: 29- Sep- 2022].
#
# [28] chandrashekhar, "Python - Flask Login Form Example", onlinetutorialspoint, 2022. [Online]. Available:
# https://www.onlinetutorialspoint.com/flask/python-flask-login-form-example.html. [Accessed: 29- Sep- 2022].
#
# [29] "NDB Query Class  |  App Engine standard environment for Python 2  |  Google Cloud", Google Cloud,
# 2022. [Online]. Available: https://cloud.google.com/appengine/docs/legacy/standard/python/ndb/queryclass. [
# Accessed: 29- Sep- 2022].
#
# [30] "Creating Entity Models  |  App Engine standard environment for Python 2  |  Google Cloud", Google Cloud,
# 2022. [Online]. Available: https://cloud.google.com/appengine/docs/legacy/standard/python/ndb/creating-entity
# -models. [Accessed: 29- Sep- 2022].
#
# [31] R. Simon, "Change color of flask.flash messages", Stack Overflow, 2022. [Online]. Available:
# https://stackoverflow.com/questions/44569040/change-color-of-flask-flash-messages. [Accessed: 29- Sep- 2022].
#
# [32] "Datastore Queries  |  Cloud Datastore Documentation  |  Google Cloud", Google Cloud, 2022. [Online].
# Available: https://cloud.google.com/datastore/docs/concepts/queries. [Accessed: 29- Sep- 2022].
#
# [33] O. Elijah Ochieng, "How to Authenticate Users in Flask with Flask-Login", freeCodeCamp.org, 2022. [Online].
# Available: https://www.freecodecamp.org/news/how-to-authenticate-users-in-flask/. [Accessed: 29- Sep- 2022].
#
# [34] Frank, "Login authentication with Flask", pythonspot, 2022. [Online]. Available:
# https://pythonspot.com/login-authentication-with-flask/. [Accessed: 29- Sep- 2022].
#
# [35] davidism, "Using Flask-WTForms, how do I style my form section of the html?", Stack Overflow, 2022. [Online].
# Available: https://stackoverflow.com/questions/34738331/using-flask-wtforms-how-do-i-style-my-form-section-of-the
# -html. [Accessed: 29- Sep- 2022].
#
# [36] "Python", Python.tutorialink.com, 2022. [Online]. Available:
# https://python.tutorialink.com/importerror-cannot-import-name-app-from-partially-initialized-module-market-most
# -likely-due-to-a-circular-import/. [Accessed: 29- Sep- 2022].
#
# [37] M. Chhabra, "Upload Files to Google Cloud Storage with Python - DZone Cloud", dzone.com, 2022. [Online].
# Available: https://dzone.com/articles/upload-files-to-google-cloud. [Accessed: 29- Sep- 2022].
#
# [38] mwhite, "How do I keep the value of a FileField after submission?", Stack Overflow, 2022. [Online]. Available:
# https://stackoverflow.com/questions/73681709/how-do-i-keep-the-value-of-a-filefield-after-submission. [Accessed:
# 29- Sep- 2022].
#
# [39] "How To Create Rounded Images", W3schools.com, 2022. [Online]. Available:
# https://www.w3schools.com/howto/howto_css_rounded_images.asp. [Accessed: 29- Sep- 2022].
#
# [40] "V4 signing process with Cloud Storage tools  |  Google Cloud", Google Cloud, 2022. [Online]. Available:
# https://cloud.google.com/storage/docs/access-control/signing-urls-with-helpers#code-samples. [Accessed: 29- Sep-
# 2022].
#
# [41] P. Pogorzelski, "Flask WTF-forms adding select and textarea", Stack Overflow, 2022. [Online]. Available:
# https://stackoverflow.com/questions/19917503/flask-wtf-forms-adding-select-and-textarea. [Accessed: 29- Sep- 2022].

# [43] "Python add elements to an Array - AskPython", AskPython, 2022. [Online]. Available:
# https://www.askpython.com/python/array/python-add-elements-to-an-array. [Accessed: 29- Sep- 2022].

# [53] Rohit, "Find index of element in array Python", Tutorial, 2022. [Online]. Available:
# https://tutorial.eyehunts.com/python/find-index-of-element-in-array-python/. [Accessed: 29- Sep- 2022].
#
# [54] R. Tripathi, I. Kaznacheev, Kerby82 and Gabriel_Ferreira, "How to 'update' or 'overwrite' a python list",
# Stack Overflow, 2022. [Online]. Available: https://stackoverflow.com/questions/25410507/how-to-update-or-overwrite
# -a-python-list. [Accessed: 29- Sep- 2022].
#
# [55] "Creating, Retrieving, Updating, and Deleting Entities  |  App Engine standard environment for Python 2  |
# Google Cloud", Google Cloud, 2022. [Online]. Available:
# https://cloud.google.com/appengine/docs/legacy/standard/python/ndb/creating-entities. [Accessed: 29- Sep- 2022].
#
# [56] r-m-n and pogo, "Dynamic default value setting for a flask form field", Stack Overflow, 2022. [Online].
# Available: https://stackoverflow.com/questions/33545520/dynamic-default-value-setting-for-a-flask-form-field. [
# Accessed: 29- Sep- 2022].
#
# [57] "Royalty Free Pictures [HD] | Download Free Images on Unsplash", Unsplash.com, 2022. [Online]. Available:
# https://unsplash.com/images/stock/royalty-free. [Accessed: 29- Sep- 2022].
#
# [58] Loremipsum.io, 2022. [Online]. Available: https://loremipsum.io/generator/. [Accessed: 29- Sep- 2022].

@forum.record_once
def seed_user_data(self):
    with client.context():
        query = User.query()
        result = query.fetch(1, keys_only=True)
        if result.__len__() == 0:
            init_users()


@forum.route('/')
def index():
    if not session.get('login_id'):
        return redirect('/login')

    user = User.get_by_id(session['login_id'])

    if user.user_profile_img != '':
        user_profile_img_url = generate_url(user.user_profile_img)

        session['user_profile_img_url'] = user_profile_img_url

    query = User.query(User.posts.date_and_time < datetime.datetime.utcnow()).order(-User.posts.date_and_time)
    result = query.fetch(8)

    return render_template('index.html', users=result, generate_url=generate_url,
                           convert_utc_to_local_time=convert_utc_to_local_time)


@forum.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('login_id'):
        return redirect('/')

    form = LoginForm()
    if form.validate_on_submit():

        login_id = form.login_id.data
        password = form.password.data

        user = User.get_by_id(login_id)
        if user and user.password == password:
            session['login_id'] = user.login_id
            session['user_name'] = user.user_name
            return redirect('/')
        else:
            flash('ID or password is invalid.')

    return render_template('auth/login.html', form=form)


@forum.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@forum.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('login_id'):
        return redirect('/')

    form = RegisterForm()
    if form.validate_on_submit():
        login_id = form.login_id.data
        user_name = form.user_name.data
        password = form.password.data
        user_profile_img = request.files['user_profile_img']

        filename = secure_filename(user_profile_img.filename)
        user_profile_img_filename = ''

        if User.query(User.login_id == login_id).fetch():
            flash('The ID already exists.')
        elif User.query(User.user_name == user_name).fetch():
            flash('The username already exists.')
        else:
            if filename != '':
                upload_profile_img(user_profile_img, login_id, filename)
                user_profile_img_filename = login_id + '_' + filename

            new_user = User(login_id=login_id, user_name=user_name, password=password,
                            user_profile_img=user_profile_img_filename, id=login_id)
            new_user.put()

            return redirect('/login')

    return render_template('auth/register.html', form=form)


@forum.route('/profile', methods=['GET', 'POST'])
def profile():
    if not session.get('login_id'):
        return redirect('/login')

    user = User.get_by_id(session['login_id'])

    form = EditPasswordForm()
    if form.validate_on_submit():
        old_password = form.old_password.data
        new_password = form.new_password.data

        if user.password == old_password:
            user.password = new_password
            user.put()
            flash('Password successfully updated.', 'success')
            return redirect('/logout')
        else:
            flash('The old password is incorrect.', 'error')

    return render_template('profile.html', user=user, form=form, generate_url=generate_url,
                           convert_utc_to_local_time=convert_utc_to_local_time)


@forum.route('/create', methods=['GET', 'POST'])
def create_post():
    if not session.get('login_id'):
        return redirect('/login')

    user = User.get_by_id(session['login_id'])
    form = CreatePostForm()
    if form.validate_on_submit():
        subject = form.subject.data
        message_text = form.message_text.data
        user_post_img = request.files['user_post_img']

        filename = secure_filename(user_post_img.filename)
        post_date_and_time = datetime.datetime.utcnow()
        user_post_img_filename = ''

        if filename != '':
            upload_post_img(user_post_img, user.login_id, str(post_date_and_time), filename)
            user_post_img_filename = user.login_id + '_' + str(post_date_and_time) + '_' + filename

        new_post = Post(subject=subject, message_text=message_text,
                        user_post_img=user_post_img_filename,
                        date_and_time=post_date_and_time)
        user.posts.insert(0, new_post)

        user.put()
        return redirect('/')

    return render_template('post/create.html', form=form)


@forum.route('/edit/<post_index>', methods=['GET', 'POST'])
def edit_post(post_index):
    if not session.get('login_id'):
        return redirect('/login')

    user = User.get_by_id(session['login_id'])

    form = EditPostForm()

    if form.validate_on_submit():
        new_subject = form.subject.data
        new_message_text = form.message_text.data
        new_user_post_img = request.files['user_post_img']

        filename = secure_filename(new_user_post_img.filename)
        post_date_and_time = datetime.datetime.utcnow()

        if filename != '':
            upload_post_img(new_user_post_img, user.login_id, str(post_date_and_time), filename)
            user_post_img_filename = user.login_id + '_' + str(post_date_and_time) + '_' + filename
        else:
            user_post_img_filename = user.posts[int(post_index)].user_post_img

        user.posts[int(post_index)].subject = new_subject
        user.posts[int(post_index)].message_text = new_message_text
        user.posts[int(post_index)].user_post_img = user_post_img_filename
        user.posts[int(post_index)].date_and_time = post_date_and_time

        user.put()
        return redirect('/')

    form.message_text.data = user.posts[int(post_index)].message_text
    return render_template('post/edit.html', form=form, post=user.posts[int(post_index)], generate_url=generate_url)
