"""Module containing language pipeline objects"""
import json
import spacy.language
from config import LANGUAGE_DATA_PATH
import iso639

with LANGUAGE_DATA_PATH.open(encoding="utf-8") as file:
    models = json.load(file)

class Language():
    """Basic NLP language model object."""

    @classmethod
    def load_model(cls) -> spacy.language.Language:
        """Load a specific language model pipeline, derived from the class name."""
        model_name = models[cls.__name__.lower()]
        return spacy.load(model_name)  
    
def match_language(iso_639_1: str) -> Language:
    """Match a language iso 639-1 to the correct `Language` object."""
    lang_name = iso639.to_name(iso_639_1)
    return eval(lang_name)

class English(Language): """English NLP model."""

class German(Language): """German NLP model."""

class Portuguese(Language): """Portuguese NLP model."""
