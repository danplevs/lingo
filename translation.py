"""Translation related functions."""
from typing import Union
from translate import Translator
from language import Language


def translate(text: str, target: Union[Language, str]):
    """Translate a given text to a target language."""
    to_lang = target if isinstance(target, str) else target.iso_639_1
    return Translator(to_lang=to_lang).translate(text).capitalize()
