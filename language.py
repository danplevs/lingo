"""Module containing language pipeline objects"""
import json
from pathlib import Path
import spacy.language


LANGUAGE_DATA_PATH = Path("./models.json")

with LANGUAGE_DATA_PATH.open(encoding="utf-8") as file:
    models = json.load(file)

class Language():
    """Basic NLP language model object."""

    @classmethod
    def load_model(cls) -> spacy.language.Language:
        """Load a specific language model pipeline, derived from the class name."""
        model_name = models[cls.__name__.lower()]
        return spacy.load(model_name)
    

class English(Language): """English NLP model."""


class German(Language): """German NLP model."""


class Portuguese(Language): """Portuguese NLP model."""
