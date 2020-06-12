from flask import render_template, redirect, request, make_response
from app import app
from app.forms import TextInputForm

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

@app.route('/word_list', methods=['GET'])
def word_list():
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
        'virus': 'noun',
    }
    words_to_be_redacted = redacted.keys()
    text_list = text.split(' ')
    matched_words = {}
    for word in words_to_be_redacted:
        for index, text_word in enumerate(text_list):
            if word.lower() == text_word.lower():
                matched_words[index] = redacted[word]
    print('matched_words', matched_words)
    keys = list(matched_words.keys())

    resp = make_response(render_template('word_list.html', title='Word List', matched_words=matched_words, indexes=keys))
    return resp

@app.route('/word_list', methods=['POST'])
def word_list_post():
    data = request.form
    original_text = request.cookies.get('text')
    text_arr = original_text.split(' ')
    for word in data:
        text_arr[int(word)] = data[word]

    new_text = ' '.join(text_arr)
    resp = make_response(redirect('/revamped'))
    resp.set_cookie('text', new_text)
    return resp

@app.route('/revamped', methods=['GET'])
def revamped():
    article_text=request.cookies.get('text')
    return render_template('revamped.html', article_text=article_text)
