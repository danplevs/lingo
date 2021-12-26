"""Module containing language pipeline objects"""
import json
from pathlib import Path
import spacy

LANGUAGE_DATA_PATH = Path("./language.json")

with LANGUAGE_DATA_PATH.open(encoding="utf-8") as file:
    languages = json.load(file)

class Language():
    """Basic NLP language model object."""
    iso_639_1: str

    @classmethod
    def load_model(cls) -> spacy.language.Language:
        """Load model pipeline."""
        model_name = languages[cls.__name__.lower()]["model"]
        return spacy.load(model_name)


class English(Language):
    """English NLP model."""
    iso_639_1 = languages["english"]["iso_639-1"]


class German(Language):
    """German NLP model."""
    iso_639_1 = languages["german"]["iso_639-1"]


class Portuguese(Language):
    """Portuguese NLP model."""
    iso_639_1 = languages["portuguese"]["iso_639-1"]
