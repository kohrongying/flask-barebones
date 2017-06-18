from flask import Blueprint, session, render_template, flash, redirect, url_for, request
from app import login_manager
from flask_login import login_required, logout_user, login_user
from app.forms import LoginForm, SignUpForm
from app.models import User
from app.helpers import save

mod = Blueprint('user', __name__, url_prefix='/user')

login_manager.login_view = 'user.login'

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

@mod.route('/login', methods=['GET', 'POSt'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.id.data)
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            flash('Logged in Successfully')
            return redirect(url_for('user.main'))
        else:
            flash('Invalid id or password')
    return render_template('user/login.html', form=form)

@mod.route('/register', methods=['GET', 'POST'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(id=form.id.data, password=form.password.data)
        if save(user):
            login_user(user)
            flash('Sign Up Successfully')
            return redirect(url_for('user.main'))
        else:
            flash('Try again')
    return render_template('user/register.html', form=form)

@mod.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash('Log out successfully')
    return redirect(url_for('index'))

@mod.route('/home', methods=['GET'])
@login_required
def main():
    return render_template('index.html')



