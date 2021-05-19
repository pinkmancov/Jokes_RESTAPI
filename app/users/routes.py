from flask import Blueprint, flash, redirect, url_for, request, abort
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash

from app import db
from app.users.models import User

users = Blueprint('users', __name__)


# User Login From URL Route
@users.route('/login', methods=['GET', 'POST'])
def login():
    pass


# User Logout
@users.route('/logout', methods=['GET'])
def logout():
    pass


# User Registration
@users.route('/registration', methods=['GET','POST'])
def registration():
    pass


# User account
@users.route('/account')
@login_required
def account():
    pass