from flask import Blueprint, flash, redirect, url_for, request, abort
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash

from app import db
from app.jokes.models import Joke

jokes = Blueprint('jokes',__name__)

# Create Joke
@jokes.route('/joke/create', methods=['GET', 'POST'])
@login_required
def create():
    pass

# Update Joke
@jokes.route('/joke/<int:joke_id>/update', methods=['GET', 'POST'])
@login_required
def update(joke_id):
    pass

# Task Deletion
@jokes.route('/joke/<int:joke_id>/delete', methods=['POST'])
@login_required
def delete(joke_id):
    pass