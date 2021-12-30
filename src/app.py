"""Main app module."""
import streamlit as st
import streamlit.components.v1 as components
from nlp import NLP
from language import LANGUAGES_SUPPORTED
from translation import FIRST_LANGUAGES_SUPPORTED, translate
from speech import text_to_speech

st.set_page_config(layout="wide")

st.sidebar.markdown('**<p style="font-family:sans-serif; font-size: 42px; font-weight: 600">lingo</p>**', unsafe_allow_html=True)
st.sidebar.markdown("**Explore grammar, translation and speech, all in one place.**")

first_language = st.sidebar.selectbox(
    label="Your first language",
    options=FIRST_LANGUAGES_SUPPORTED,
    index=FIRST_LANGUAGES_SUPPORTED.index("English"),
)

sentence = st.text_area(
    label="Type the sentence you wanna learn",
    value="Ein Engländer, ein Schotte und ein Ire betreten eine Bar",
    max_chars=1000,
    height=150,
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
