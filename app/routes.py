from flask import render_template, redirect, request, make_response
from app import app
from app.forms import TextInputForm, WordForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = TextInputForm()
    if form.validate_on_submit():
        # TODO: add some kind of error handling/validation
        text = form.user_input.data
        resp = make_response(redirect('/word_list'))
        resp.set_cookie('text', text)
        return resp
    return render_template('index.html', title='Home', form=form)

@app.route('/word_list', methods=['GET', 'POST'])
def word_list():
    form = WordForm()
    if form.validate_on_submit():
        text = form.matched_word.data
        resp = make_response(redirect('revamped.html'))
        resp.set_cookie('article_text', article_text)
        return resp
    text = request.cookies.get('text')
    redacted = {
        'coronavirus': 'noun',
        'economy': 'noun',
        'infection': 'noun',
        'fever': 'noun',
        'death': 'noun',
        'quarantine': 'noun',
        'stocks':'noun_plural',
        'hands':'noun_plural',
        'masks':'noun_plural',
        'restrictions': 'noun_plural',
        'Covid-19':'proper_noun',
        'Donald Trump':'proper_noun',
        'Trump':'proper_noun',
        'Mike Pence':'proper_noun',
        'Pence':'proper_noun',
        'New York':'proper_noun',
        'Wuhan': 'proper_noun',
        '100,000': 'number',
        'six': 'number',
        'test': 'verb',
        'die': 'verb',
        'wash': 'verb',
        'sick': 'adjective',
        'federal': 'adjective',
        'deadly': 'adverb',
    }
    words_to_be_redacted = redacted.keys()
    text_list = text.split(' ')
    matched_words = {}
    for word in words_to_be_redacted:
        for index, text_word in enumerate(text_list):
            if word.lower() == text_word.lower():
                matched_words[index] = redacted[word]
    print('matched_words', matched_words)
    resp = make_response(render_template('word_list.html', title='Word List', form=form, matched_words=matched_words))
    # resp.set_cookie('matched_words', matched_words)
    return resp

@app.route('/revamped', methods=['GET'])
def revamped():
    article_text=request.cookies.get('article_text')
    render_template('revamped.html', article_text=article_text)

# @app.route('/word_list', methods=['POST'])
# def word_list():
#     if form.validate_on_submit():
#         text = form.matched_word.data
#         resp = make_response(redirect('revamped.html'))
#         resp.set_cookie('article_text', article_text)
#         return resp

#POST / submit form & redact words list
#GET /libs form of redcacted words
#POST /libs fill in the missing words
#GET /final display full text with replaced words


# from flask import make_response

# @app.route('/')
# def index():
#     resp = make_response(render_template(...))
#     resp.set_cookie('username', 'the username')
#     return resp
