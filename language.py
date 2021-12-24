"""Module containing language pipeline objects"""
import json
from pathlib import Path
import spacy

LANGUAGE_DATA_PATH = Path("./language.json")

with LANGUAGE_DATA_PATH.open(encoding="utf-8") as file:
    languages = json.load(file)

class Language():
    """Basic NLP language model object."""
    @classmethod
    def load_model(cls) -> spacy.language.Language:
        """Load model pipeline"""
        model_name = languages[cls.__name__.lower()]["model"]
        return spacy.load(model_name)


class English(Language):
    """English NLP model."""


class German(Language):
    """German NLP model."""
    
class Portuguese(Language):
    """Portuguese NLP model."""
