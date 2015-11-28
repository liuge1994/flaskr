from flask import render_template
from . import auth
from flask.ext.login import login_required

@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'

@auth.route('/login')
def login():
    return render_template('auth/login.html')