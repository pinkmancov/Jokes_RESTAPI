from flask import Blueprint, flash, request, redirect, url_for, render_template, abort
from flask_login import current_user, login_required

from app import db
from app.jokes.models import Joke
from app.jokes.forms import JokeForm

jokes = Blueprint('jokes', __name__)


# Добавить шутку
@jokes.route('/joke/create', methods=['GET', 'POST'])
@login_required
def create():

    form_joke = JokeForm()
    user_id = current_user.id
    if form_joke.validate_on_submit():
        joke = Joke(title=form_joke.title.data,
                    description=form_joke.description.data,
                    user_id=user_id)

        # Добавляем в базу данных
        try:
            db.session.add(joke)
            db.session.commit()
            flash("Ваша шутка добавлена!", "Успешно!")
            return redirect(url_for('main.index'))
        except IndexError:
            flash("Возникла проблема при создании шутки", "Внимание!")
    return render_template('jokes/create.html', title='Добавить шутку', \
                           form=form_joke, legend='Добавить шутку')


# Обновить шутку
@jokes.route('/joke/<int:joke_id>/update', methods=['GET', 'POST'])
@login_required
def update(joke_id):
    joke = db.session.query(Joke).filter(Joke.id == joke_id).first()

    if request.method == 'POST':
        form_joke = JokeForm(formdata=request.form, obj=joke_id)
        form_joke.populate_obj(joke)

        db.session.commit()
        flash("Ваша шутка отредактирована!", "Успешно")
        return redirect(url_for('main.index', joke_id=joke.id))

    form_joke = JokeForm(obj=joke)
    return render_template('jokes/update.html', title='Редактирование шутки',
                           form=form_joke, joke=joke, legend='Шутка отредактирована')


# Удалить шутку
@jokes.route('/joke/<int:joke_id>/delete', methods=['POST'])
@login_required
def delete(joke_id):

    joke = db.session.query(Joke).get_or_404(joke_id)

    try:
        db.session.delete(joke)
        db.session.commit()
        flash("Ваша шутка удалена!", "Успешно")
        return redirect(url_for('main.index'))
    except IndexError:
        flash("Возникла непредвиденная ошибка при удалении!", "Внимание")
