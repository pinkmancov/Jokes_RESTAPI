from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired


class JokeForm(FlaskForm):
    """Форма создания/редактирования шутки"""
    title = StringField('Название шутки', validators=[InputRequired()])
    description = TextAreaField('Текст шутки', validators=[InputRequired()])