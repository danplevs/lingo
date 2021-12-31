"""NLP module containing pos tagging, translation and text to speech functions."""
from typing import List, DefaultDict, Union
from collections import defaultdict

import spacy
from spacy.tokens import Doc, Span
from spacy import displacy
from pandas import DataFrame
from language import fetch_model
from translation import detect_language


class NLP:
    """NLP processor and renderer."""

    def __init__(self, text: str) -> None:
        self.text: str = text
        self.language: str = detect_language(self.text)
        self.model: str = fetch_model(self.language)
        self.nlp: spacy.language.Language = spacy.load(self.model)
        self.doc: Doc = self.nlp(self.text)

    def process(self, doc: Doc = None) -> DefaultDict[str, List[str]]:
        """Process part of speech tags."""
        if not doc:
            doc = self.doc

        part_of_speech: DefaultDict[str, List[str]] = defaultdict(list)
        for token in doc:
            part_of_speech["Text"].append(token.text)
            part_of_speech["Lemma"].append(token.lemma_)
            part_of_speech["Part of speech"].append(
                spacy.explain(token.tag_) + f" ({token.pos_})"
            )
            part_of_speech["Syntactic dependency"].append(
                token.dep_.lower()
                if spacy.explain(token.dep_) is None
                else spacy.explain(token.dep_) + f" ({token.dep_})"
            )
        return part_of_speech

    def vocab_chart(self, doc: Union[Span, Doc] = None) -> DataFrame:
        """Create the vocabulary chart of `self.text`."""
        if not doc:
            doc = self.doc
        return DataFrame.from_dict(self.process(doc))


    def render(self, doc: Union[Span, Doc] = None) -> str:
        """Render a figure of the sentence dependencies and part of speech as a HTML string."""
        if not doc:
            doc = self.doc
        return displacy.render(doc)
