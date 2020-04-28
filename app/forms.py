from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired

class TextInputForm(FlaskForm):
    user_input = StringField('Enter your text here', validators=[DataRequired()])
    submit = SubmitField('Submit')

class WordForm(FlaskForm):
    write_your_own = FieldList(StringField(validators=[DataRequired()]), min_entries=1)
    submit = SubmitField('Submit')
