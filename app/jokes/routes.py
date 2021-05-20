from flask import Blueprint, flash, request, redirect, url_for, render_template, abort
from flask_login import current_user, login_required
import requests
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
        joke_add = Joke(title=form_joke.title.data,
                        description=form_joke.description.data,
                        user_id=user_id)

        # Добавляем в базу данных
        try:
            db.session.add(joke_add)
            db.session.commit()
            flash("Ваша шутка добавлена!")
            return redirect(url_for('main.index'))
        except IndexError:
            flash("Возникла проблема при создании шутки")
    return render_template('jokes/create.html', title='Добавить шутку', \
                           form=form_joke, legend='Добавить шутку')


# Генерация шутки с внешнего сервиса
@jokes.route('/joke/generation')
@login_required
def generation():
    res = requests.get('https://geek-jokes.sameerkumar.website/api')
    print(res.text)
    user_id = current_user.id
    joke_gen = Joke(title='Сгенерированая шутка',
                    description=res.text,
                    user_id=user_id)
    # Добавляем в базу данных
    try:
        db.session.add(joke_gen)
        db.session.commit()
        flash("Ваша шутка добавлена!")
        return redirect(url_for('main.index'))
    except IndexError:
        flash("Возникла проблема при создании шутки", "Внимание!")


# Обновить шутку
@jokes.route('/joke/<int:joke_id>/update', methods=['GET', 'POST'])
@login_required
def update(joke_id):
    joke_upd = db.session.query(Joke).filter(Joke.id == joke_id).first()
    joke_list = db.session.query(Joke).filter_by(user_id=current_user.id).all()
    joke_list_all = db.session.query(Joke).all()

    # Проверка существования
    if joke_upd in joke_list_all:
        pass
    else:
        return abort(404)

    # Проверка доступа
    if joke_upd in joke_list:
        pass
    else:
        return abort(403)

    if request.method == 'POST':
        form_joke = JokeForm(formdata=request.form, obj=joke_id)
        form_joke.populate_obj(joke_upd)

        db.session.commit()
        flash("Ваша шутка отредактирована!", "Успешно")
        return redirect(url_for('main.index', joke_id=joke_upd.id))

    form_joke = JokeForm(obj=joke_upd)
    return render_template('jokes/update.html', title='Редактирование шутки',
                           form=form_joke, joke=joke_upd, legend='Шутка отредактирована')


# Удалить шутку
@jokes.route('/joke/<int:joke_id>/delete', methods=['POST'])
@login_required
def delete(joke_id):
    joke_del = db.session.query(Joke).get_or_404(joke_id)

    try:
        db.session.delete(joke_del)
        db.session.commit()
        flash("Ваша шутка удалена!")
        return redirect(url_for('main.index'))
    except IndexError:
        flash("Возникла непредвиденная ошибка при удалении!")


# Получить шутку по ID
@jokes.route('/joke/<joke_id>', methods=['GET'])
@login_required
def joke(joke_id):
    joke_view = db.session.query(Joke).filter(Joke.id == joke_id).first()
    joke_list = db.session.query(Joke).filter_by(user_id=current_user.id).all()
    joke_list_all = db.session.query(Joke).all()

    # Проверка существования
    if joke_view in joke_list_all:
        pass
    else:
        return abort(404)

    # Проверка доступа
    if joke_view in joke_list:
        pass
    else:
        return abort(403)

    form_joke = JokeForm(obj=joke_view)
    return render_template('jokes/views.html', title='Просмотр шутки',
                           form=form_joke, joke=joke_view, legend='Просмотр шутки')