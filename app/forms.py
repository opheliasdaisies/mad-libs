from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TextInputForm(FlaskForm):
    user_input = StringField('Enter your text here', validators=[DataRequired()])
    submit = SubmitField('Submit')

class WordForm(FlaskForm):
    matched_word = StringField('Write your own', validators=[DataRequired()])
    submit = SubmitField('Submit')
