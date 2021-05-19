from flask import Blueprint, redirect, url_for, render_template, request, abort
from flask_login import current_user, login_required

from app import db
from app.jokes.models import Joke

main = Blueprint('main',__name__)


# Home Page URL Route
@main.route('/', methods=['GET'])
def home():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    else:
        return render_template('main/home.html')

# Home Page URL Route
@main.route('/index', methods=['GET'])
@login_required
def index():
    user_id = current_user.id
    jokes = db.session.query(Joke).filter(Joke.user_id == user_id).all()
    return render_template('main/index.html', jokes=jokes)