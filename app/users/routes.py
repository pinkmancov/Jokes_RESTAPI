from flask import Blueprint, flash, redirect, url_for, request, abort
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash
from werkzeug.urls import url_parse

from app import db
from app.users.models import User
from app.users.forms import LoginForm, RegistrationForm

users = Blueprint('users', __name__)


# User Login From URL Route
@users.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    # Разрешаем вход в систему если проверка прошла успешно
    if login_form.validate_on_submit():
        user = db.session.query(User) \
                .filter_by(username=login_form.username.data).first()
        if user is None or not user \
                .check_password(login_form.password.data):
            flash("Неверное имя пользователя или пароль", "Внимание")
            return redirect(url_for('users.login'))
        login_user(user, remember=login_form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
#   return render_template('',form=login_form)


# User Logout
@users.route('/logout', methods=['GET'])
def logout():
    pass


# User Registration
@users.route('/registration', methods=['GET','POST'])
def registration():
    reg_form = RegistrationForm()

    # Обновляем БД в случае успешной проверки
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # Hash пароля
        password_hash = generate_password_hash(password)

        # Добавим username и hashed passowd в БД
        new_user = User(username=username,
                        password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()

        flash("Спасибо! Теперь вы являетесь зарегистрированным пользователем", "Успешно")
        return redirect(url_for('users.login'))
#   return render_template()

# User account
@users.route('/account')
@login_required
def account():
    pass