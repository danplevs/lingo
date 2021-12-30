import streamlit as st
import streamlit.components.v1 as components
from nlp import NLP
from language import models
from translation import translate
from speech import text_to_speech

st.set_page_config(layout="wide")

langs_supported = [lang.capitalize() for lang in models.keys()]

main_language = st.sidebar.selectbox(
    label="Your first language", options=langs_supported
)

st.title("Lingo: learn a new language")

sentence = st.text_area(
    label="Type the sentence you want to learn",
    value="An Englishman, a Scotsman and a Irishman walk into a bar.",
    max_chars=5000,
    height=250,
)
if not sentence:
    st.warning("A sentence is needed to run lingo.")
    st.stop()
    
nlp = NLP(sentence)

st.header("Translation")
st.info(translate(sentence, target=main_language))

st.header("Pronunciation")
st.audio(text_to_speech(sentence))


st.header("Vocabulary chart")
st.dataframe(nlp.vocab_chart(), width=1000)

st.header("Syntactic dependencies")
components.html(nlp.render(), height=450, scrolling=True)
