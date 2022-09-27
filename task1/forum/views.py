from flask import render_template, flash, Blueprint, redirect, session
from .models import LoginForm, init_users, User, RegisterForm
from google.cloud import ndb

forum = Blueprint('forum', __name__, template_folder="templates/forum")
client = ndb.Client()


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

        loginid = form.login_id.data
        password = form.password.data

        user = User.get_by_id(loginid)
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
    return render_template('auth/register.html', form=form)
