from flask import render_template, request, flash

from task1.forum import forms

from task1.forum.__init__ import app


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm(request.form)

    if request.method == 'POST':
        loginid = form.loginID.data
        password = form.password.data

    if form.validate():
        if form.loginID.data == 'admin' and form.password.data == 'admin':
            flash('Hello ')
        else:
            flash('All fields required')

    return render_template('auth/login.html', form=form)
