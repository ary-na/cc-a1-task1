from flask import render_template

from task1.__init__ import app


@app.route('/login')
def login():
    return render_template('auth/login.html')