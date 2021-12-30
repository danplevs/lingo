"""Main app module."""
import streamlit as st
import streamlit.components.v1 as components
from nlp import NLP
from language import LANGUAGES_SUPPORTED
from translation import FIRST_LANGUAGES_SUPPORTED, translate
from speech import text_to_speech

st.set_page_config(layout="wide")

first_language = st.sidebar.selectbox(
    label="Your first language", options=FIRST_LANGUAGES_SUPPORTED
)

st.title("Lingo: learn a new language")

sentence = st.text_area(
    label="Type the sentence you want to learn",
    value="An Englishman, a Scotsman and a Irishman walk into a bar.",
    max_chars=5000,
    height=250,
)

with st.expander("Input languages supported"):
    st.write(LANGUAGES_SUPPORTED)

if not sentence:
    st.warning("A sentence is needed to run lingo.")
    st.stop()

nlp = NLP(sentence)

st.header("Translation")
st.info(translate(sentence, target=first_language))

st.header("Pronunciation")
st.audio(text_to_speech(sentence))



st.header("Vocabulary chart")
vocab_chart = nlp.vocab_chart()
styler = vocab_chart.style.hide_index()
st.write(styler.to_html(), unsafe_allow_html=True)

st.header("Syntactic dependencies")
components.html(nlp.render(), height=450, scrolling=True)
