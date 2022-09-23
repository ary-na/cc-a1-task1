import datetime

from flask import Blueprint, request, url_for, redirect, render_template, flash
from flask import render_template, request, flash
from google.cloud import datastore

from .models import LoginForm, init_users

forum = Blueprint('forum', __name__, template_folder="templates/forum")


@forum.route('/')
def index():
    client = datastore.Client()
    query = client.query(kind="user")
    results = list(query.fetch(1))
    if results.__len__() == 0:
        init_users()

    return render_template('index.html')


@forum.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST':
        loginid = form.loginID.data
        password = form.password.data

    if form.validate():
        if form.loginID.data == 'admin' and form.password.data == 'admin':
            flash('Hello ')
        else:
            flash('All fields required')

    return render_template('auth/login.html', form=form)


@forum.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html')
