import datetime

import pytz
from flask import render_template, flash, Blueprint, redirect, session, request
from werkzeug.utils import secure_filename
from .models import LoginForm, init_users, User, RegisterForm, upload_profile_img, generate_url, CreatePostForm, \
    upload_post_img, Post, convert_utc_to_local_time, EditPasswordForm
from google.cloud import ndb, storage

forum = Blueprint('forum', __name__, template_folder="templates/forum")
client = ndb.Client()
storage_client = storage.Client.from_service_account_json(
    json_credentials_path='/Users/ariannajafi/Downloads/cc-a1-task1-362004-897b592819f6.json')


# storage_client = storage.Client()


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

    query = User.query(User.posts.date_and_time <= datetime.datetime.utcnow()).order(-User.posts.date_and_time)
    result = query.fetch(10)

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
            flash('Password successfully updated.')
        else:
            flash('The old password is incorrect.')

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
