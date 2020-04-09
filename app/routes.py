from flask import render_template, redirect
from app import app
from app.forms import TextInputForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = TextInputForm()
    if form.validate_on_submit():
        # TODO: add some kind of error handling/validation
        print(form.user_input)
        return redirect('/word_list')
    return render_template('index.html', title='Home', form=form)

@app.route('/word_list', methods=['GET'])
def word_list():
    return 'Hello World!'
    # return render_template('word_list.html', title='Word List')
    #, form=WordForm())

#POST / submit form & redact words list
#GET /libs form of redcacted words
#POST /libs fill in the missing words
#GET /final display full text with replaced words
