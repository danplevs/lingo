"""Main app module."""
import streamlit as st
import streamlit.components.v1 as components
from nlp import NLP
from language import LANGUAGES_SUPPORTED
from translation import FIRST_LANGUAGES_SUPPORTED, detect_language, translate
from speech import text_to_speech
import iso639

st.set_page_config(layout="wide")

# Sidebar content
st.sidebar.markdown(
    '**<p style="font-family:sans-serif; font-size: 42px; font-weight: 600">lingo</p>**',
    unsafe_allow_html=True,
)
st.sidebar.markdown("**Explore grammar, translation and speech, all in one place.**")

DEFAULT_LANGUAGE_INDEX = FIRST_LANGUAGES_SUPPORTED.index("English - en")

trans_language = iso639.to_iso639_1(st.sidebar.selectbox(
    label="Your first language",
    options=FIRST_LANGUAGES_SUPPORTED,
    index=DEFAULT_LANGUAGE_INDEX).split(" - ")[0]
)

split_sents = st.sidebar.checkbox(label="Split sentences", value=True)

use_first_lang = st.sidebar.checkbox(
    label="Use first language for translation", value=True
)
if not use_first_lang:
    trans_language = st.sidebar.selectbox(
        label="Select a language for translation",
        options=FIRST_LANGUAGES_SUPPORTED,
        index=DEFAULT_LANGUAGE_INDEX,
    )


# Input area
text = st.text_area(
    label="Type the text you wanna learn",
    value="Ein Engländer, ein Schotte und ein Ire betreten eine Bar",
    max_chars=1000,
    height=150).strip()

with st.expander("Input languages supported"):
    st.write(LANGUAGES_SUPPORTED.items())

if not text:
    st.error("A sentence is needed to run lingo.")
    st.stop()
elif detect_language(text) not in LANGUAGES_SUPPORTED.keys():
    st.error("Unsupported language.")
    st.stop()

nlp = NLP(text)

# Translation
st.header("Translation")
if not split_sents:
    st.info(translate(nlp.text, target=trans_language))

else:
    for sent in nlp.doc.sents:
        st.info(translate(sent.text, target=trans_language))

# Pronunciation
st.header("Pronunciation")
if not split_sents:
    st.audio(text_to_speech(nlp.text))
else:
    for sent in nlp.doc.sents:
        st.markdown(f"> {sent}")
        st.audio(text_to_speech(sent.text))

# Vocab chart
st.header("Vocabulary chart")
if not split_sents:
    vocab_chart = nlp.vocab_chart()
    styler = vocab_chart.style.hide_index()
    st.write(styler.to_html(), unsafe_allow_html=True)
else:
    for sent in nlp.doc.sents:
        vocab_chart = nlp.vocab_chart(sent)
        styler = vocab_chart.style.hide_index()
        st.markdown(f"> {sent}")
        st.write(styler.to_html(), unsafe_allow_html=True)
        st.write("")
        # st.dataframe(vocab_chart)

# Syntactic deps
st.header("Syntactic dependencies")
if not split_sents:
    components.html(nlp.render(), height=450, scrolling=True)
else:
    for sent in nlp.doc.sents:
        components.html(nlp.render(sent), height=450, scrolling=True)
