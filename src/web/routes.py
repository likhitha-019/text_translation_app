from flask import Blueprint, render_template, request, redirect, url_for
from model.translator import Translator
from utils.languages import get_language_list

web_bp = Blueprint('web', __name__)
translator = Translator()

@web_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        source_language = request.form.get('source_language')
        target_language = request.form.get('target_language')
        text_to_translate = request.form.get('text_to_translate')
        
        if source_language and target_language and text_to_translate:
            translated_text = translator.translate_to(target_language, text_to_translate)
            return render_template('index.html', translated_text=translated_text, 
                                   source_language=source_language, 
                                   target_language=target_language,
                                   languages=get_language_list())
    
    return render_template('index.html', languages=get_language_list())