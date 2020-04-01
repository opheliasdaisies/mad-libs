from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    text = {'text': 'Go away coronavirus'}
    return render_template('index.html', title='Home', text=text)
