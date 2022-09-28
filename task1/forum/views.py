from flask import render_template, flash, Blueprint, redirect, session, request, send_from_directory
from werkzeug.utils import secure_filename
from ..main import app
from .models import LoginForm, init_users, User, RegisterForm
from google.cloud import ndb, storage
import os.path

forum = Blueprint('forum', __name__, template_folder="templates/forum")
client = ndb.Client()
storage_client = storage.Client.from_service_account_json(
    json_credentials_path='/Users/ariannajafi/Downloads/cc-a1-task1-362004-897b592819f6.json')


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
    return render_template('index.html')


@forum.route('/login', methods=['GET', 'POST'])
def login():
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

        if User.query(User.login_id == login_id).fetch():
            flash('The ID already exists.')
        elif User.query(User.user_name == user_name).fetch():
            flash('The username already exists.')
        else:
            filename = secure_filename(user_profile_img.filename)

            bucket = storage_client.get_bucket('forum_image_bucket')
            blob = bucket.blob(login_id + "_" + filename)
            blob.upload_from_file(user_profile_img, content_type='image/jpeg')

            new_user = User(login_id=login_id, user_name=user_name, password=password,
                            user_profile_img=filename, id=login_id)
            new_user.put()

            return redirect('/login')

    return render_template('auth/register.html', form=form)
