# pylint: disable=no-value-for-parameter
"""Routes for user authentication."""

from flask import (Blueprint, current_app, redirect, render_template, request,
                   session, url_for)
from flask_login import LoginManager, login_user, logout_user

from src.database.models import User
from src.database.querys import UserQuerys

auth = Blueprint(
    'auth', __name__,
    template_folder='templates',
    static_folder='static',
)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.init_app(current_app)

@current_app.before_request
def check_valid_login():
    """ Check if user have a valid login."""
    login_valid = '_user_id' in session # or whatever you use to check valid login
    rules = (
        request.endpoint and
        'static' not in request.endpoint and
        not login_valid and
        not getattr(current_app.view_functions[request.endpoint], 'is_public', False))

    match rules:
        case True:
            return render_template('pages/auth/login.html')

def public_endpoint(function):
    """Decoretor for public routes"""
    function.is_public = True
    return function

@login_manager.user_loader
def load_user(user_id):
    """Manage users in database."""
    return UserQuerys.get_by_id(user_id)


@auth.route('/login', methods=['GET', 'POST'])
@public_endpoint
def login():
    """Loggin user in system"""
    match request.method:
        case 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            user = UserQuerys.get_by_email(email)
            pass_crypt = user.check_password(password)

            match [user, pass_crypt]:
                case [User(email), True]:
                    login_user(user)
                    return redirect('/')

    return render_template('pages/auth/login.html')


@auth.route('/create_user', methods=['GET', 'POST'])
def create_user():
    """Register new user."""
    match request.method:
        case 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            if not UserQuerys.get_by_email(email):
                UserQuerys.create(name, email, password)

    return redirect(url_for('dashboard.dashboard'))

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    """Logout user."""
    logout_user()
    return render_template('pages/auth/login.html')
