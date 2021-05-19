from flask import Blueprint, redirect, url_for, render_template, request, abort
from flask_login import current_user, login_required

from app import db
from app.users.models import User
from app.jokes.models import Joke

main = Blueprint('main',__name__)


# Home Page URL Route
@main.route('/', methods=['GET'])
def home():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    else:
        return render_template()

# Home Page URL Route
@main.route('/index', methods=['GET'])
@login_required
def index():
    pass