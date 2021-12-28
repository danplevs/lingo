"""Environment configuration settings."""
import os
from pathlib import Path
import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())
GOOGLE_CREDENTIALS_PATH = Path(os.getenv("GOOGLE_CREDENTIALS_PATH"))
LANGUAGE_DATA_PATH = Path(os.getenv("LANGUAGE_DATA_PATH"))
