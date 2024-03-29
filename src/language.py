"""Module containing languages and models."""
import json
from pathlib import Path
from typing import Dict
import iso639

ROOT = Path(__file__).parents[1]
LANGUAGE_DATA_PATH = ROOT / "models" / "models.json"

with LANGUAGE_DATA_PATH.open(encoding="utf-8") as file:
    MODELS: Dict[str, str] = json.load(file)

LANGUAGES_SUPPORTED = {lang:iso639.to_name(lang).title() for lang in MODELS.keys()}

def fetch_model(language_code: str):
    """Helper function to fetch the spacy model name that matches text language."""
    return MODELS[language_code]
