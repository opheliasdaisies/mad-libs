from flask import render_template
from app import app
from app.forms import TextInputForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', form=TextInputForm())
