from flask import render_template, reditect, request, url_for, flash
from flask.ext.login import login_required, login_user
from . import auth
from ..models import User 
from .forms import LoginForm


@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'

@auth.route('/login')
def login():
    return render_template('auth/login.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return reditect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)