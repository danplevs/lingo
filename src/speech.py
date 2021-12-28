"""Text to speech functions."""
from io import BytesIO
from gtts import gTTS
from translation import detect_language


def text_to_speech(text: str):
    """Convert text into a natural sounding speech."""
    mp3_fp = BytesIO()
    tts = gTTS(text, lang=detect_language(text))
    return tts.write_to_fp(mp3_fp)
