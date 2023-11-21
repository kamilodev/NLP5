from googletrans import Translator

translator = Translator()


def translate_text(text, dest="en"):
    try:
        lang = translator.detect(text).lang
        return text if lang == dest else translator.translate(text, dest=dest).text
    except:
        return text
