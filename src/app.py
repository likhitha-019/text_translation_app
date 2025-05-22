from flask import Flask, render_template, request
from model.translator import Translator
from utils.languages import get_language_list

app = Flask(__name__)

translator = Translator()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', translated_text="", languages=get_language_list())

@app.route('/translate', methods=['POST'])
def translate():
    source_language = request.form['source_language']
    target_language = request.form['target_language']
    text_to_translate = request.form['text']
    translated_text = translator.translate_to(source_language, target_language, text_to_translate)
    return render_template('index.html', translated_text=translated_text, languages=get_language_list())

if __name__ == '__main__':
    app.run(debug=True)