import datetime

from flask import Blueprint, request, url_for, redirect, render_template, flash
from flask import render_template, request, flash

from .models import LoginForm

forum = Blueprint('forum', __name__, template_folder="templates/forum")


@forum.route('/')
def index():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    dummy_times = [datetime.datetime(2018, 1, 1, 10, 0, 0),
                   datetime.datetime(2018, 1, 2, 10, 30, 0),
                   datetime.datetime(2018, 1, 3, 11, 0, 0),
                   ]

    return render_template('index.html', times=dummy_times)


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
