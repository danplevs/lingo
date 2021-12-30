"""Module containing language pipeline objects"""
import json
from typing import Dict
import iso639
from config import LANGUAGE_DATA_PATH


with LANGUAGE_DATA_PATH.open(encoding="utf-8") as file:
    MODELS: Dict[str, str] = json.load(file)

LANGUAGES_SUPPORTED = sorted([lang.title() for lang in MODELS.keys()])

def fetch_model(language: str):
    """Helper function to fetch the spacy model name that matches text language."""
    lang_name = iso639.to_name(language).lower()
    return MODELS[lang_name]
