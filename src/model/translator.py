from transformers import MarianMTModel, MarianTokenizer

class Translator:
    def __init__(self):
        # Add more models as needed
        self.models = {
            ("English", "French"): (
                MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-fr"),
                MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-fr")
            ),
            ("French", "English"): (
                MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-fr-en"),
                MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-fr-en")
            ),
            ("English", "Spanish"): (
                MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-es"),
                MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-es")
            ),
            ("Spanish", "English"): (
                MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-es-en"),
                MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-es-en")
            ),
            ("English", "German"): (
                MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-de"),
                MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-de")
            ),
            ("German", "English"): (
                MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-de-en"),
                MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-de-en")
            ),
            # Add more pairs as needed
        }

    def translate_to(self, source_language, target_language, text):
        if source_language == target_language:
            return text  # No translation needed
        key = (source_language, target_language)
        if key not in self.models:
            return "Translation direction not supported."
        model, tokenizer = self.models[key]
        inputs = tokenizer([text], return_tensors="pt", padding=True)
        translated = model.generate(**inputs)
        tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)[0]
        return tgt_text