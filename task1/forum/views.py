import datetime

from flask import Blueprint, request, url_for, redirect, render_template, flash
from flask import render_template, request, flash
from google.cloud import datastore

from .models import LoginForm

forum = Blueprint('forum', __name__, template_folder="templates/forum")


@forum.route('/')
def index():
    client = datastore.Client()
    key = client.key('user')
    user = client.get(key)
    if user["id"] == 's39109020':
        entity = datastore.Entity(key=client.key('user'))

        entity.update({
            'id': '22222222'
        })

        client.put(entity)

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
