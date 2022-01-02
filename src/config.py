"""Environment configuration settings."""
import os
from pathlib import Path
import dotenv

ROOT = Path(__file__).parents[1]

dotenv.load_dotenv(dotenv.find_dotenv())
GOOGLE_CREDENTIALS_PATH = ROOT / os.getenv("GOOGLE_CREDENTIALS_PATH")
LANGUAGE_DATA_PATH = ROOT / os.getenv("LANGUAGE_DATA_PATH")
