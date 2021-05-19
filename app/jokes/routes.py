from flask import Blueprint, flash, redirect, url_for, request, abort
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash

from app import db
from app.jokes.models import Joke
from app.jokes.forms import JokeForm
from app.users.models import User

jokes = Blueprint('jokes',__name__)

# Добавить шутку
@jokes.route('/joke/create', methods=['GET', 'POST'])
@login_required
def create():
    # Checking the user to superuser
    if current_user.is_superuser:
        pass
    else:
        return abort(403)

    # List users for create task
    user_list = [(i.id, i.username) for i in db.session.query(User).all()]
    form_joke = JokeForm()
    form_joke.user_id.choices = user_list
    if form_joke.validate_on_submit():
        joke = Joke(title=form_joke.title.data,
                    description=form_joke.description.data,
                    user_id=form_joke.user_id.data)

        # Adding In DB
        try:
            db.session.add(joke)
            db.session.commit()
            flash("Ваша шутка добавлена!", "Успешно!")
            return redirect(url_for('main.index'))
        except IndexError:
            flash("Возникла проблема при создании шутки", "Внимание!")
#    return render_template('', title='Доьавить шутку',
#                          form=form_joke, legend='Добавить шутку')


# Обновить шутку
@jokes.route('/joke/<int:joke_id>/update', methods=['GET', 'POST'])
@login_required
def update(joke_id):
    pass

# Удалить шутку
@jokes.route('/joke/<int:joke_id>/delete', methods=['POST'])
@login_required
def delete(joke_id):
    pass