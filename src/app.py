import streamlit as st
from language import models
from translation import translate
from speech import text_to_speech

langs_supported = [lang.capitalize() for lang in models.keys()]

main_language = st.sidebar.selectbox(
    label="Your main language", options=langs_supported
)

st.title("Lingo: learn a new language")

sentence = st.text_area(
    label="Type the sentence you want to learn", max_chars=5000, height=250
)

st.header("Translation")
if st.button("Translate"):
    translation = translate(sentence, target=main_language)
    st.info(translation)

st.header("Pronunciation")
st.audio(text_to_speech(sentence))
