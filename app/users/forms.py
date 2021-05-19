from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, EqualTo, ValidationError

from app import db
from app.users.models import User

class LoginForm(FlaskForm):
    """Форма входа"""

    username = StringField('Имя пользователя', validators=[InputRequired()])
    password = PasswordField('Пароль', validators=[InputRequired()])
    remember_me = BooleanField('Запомнить меня', default=False)
    submit = SubmitField('Войти')

class RegistrationForm(FlaskForm):
    """Форма регистрации"""

    username = StringField('Имя пользователя', validators=[InputRequired()])
    password = PasswordField('Пароль', validators=[InputRequired()])
    confirm_password = PasswordField('Подтвердите пароль',
                                     validators=[InputRequired(),
                                                 EqualTo('password',
                                                         message='Пароли должны совпадать')])
    submit = SubmitField('Регистрация')

    # функция проверки логина на совпадение
    def validate_username(self, username):
        pass