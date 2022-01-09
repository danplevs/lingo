"""Translation related functions."""
from google.cloud import translate_v2
from config import GOOGLE_CREDENTIALS_PATH


translate_client = translate_v2.Client.from_service_account_json(
    GOOGLE_CREDENTIALS_PATH
)

FIRST_LANGUAGES_SUPPORTED = sorted(
    [
        f"{lang['name']} - {lang['language']}"
        for lang in translate_client.get_languages()
    ]
)

def detect_language(text: str) -> str:
    """Detect the language of a given string and return the `Language` object that matches it."""
    result = translate_client.detect_language(text)
    return result["language"]

def translate(text: str, target: str):
    """Translate a given text to a target language (iso 639-1 code)."""
    return translate_client.translate(text, target)["translatedText"]
