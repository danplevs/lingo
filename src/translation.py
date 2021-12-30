"""Translation related functions."""
from deep_translator import GoogleTranslator
from google.cloud import translate_v2
from config import GOOGLE_CREDENTIALS_PATH

FIRST_LANGUAGES_SUPPORTED = [lang.title() for lang in GoogleTranslator.get_supported_languages()]

def detect_language(text: str) -> str:
    """Detect the language of a given string and return the `Language` object that matches it."""
    translate_client = translate_v2.Client.from_service_account_json(GOOGLE_CREDENTIALS_PATH)
    result = translate_client.detect_language(text)
    return result["language"]

def translate(text: str, target: str):
    """Translate a given text to a target language (iso 639-1 code)."""
    return GoogleTranslator(source="auto", target=target).translate(text)
