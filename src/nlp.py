"""NLP module containing pos tagging, translation and text to speech functions."""
from typing import List, DefaultDict
from collections import defaultdict

import spacy
from spacy.tokens import Doc
import pandas as pd
from language import Language, match_language
from translation import detect_language


class NLP:
    """NLP processor and renderer."""

    def __init__(self, text: str) -> None:
        self.text: str = text
        self.language: Language = match_language(detect_language(text))
        self.nlp: spacy.language.Language = self.language.load_model()

    def process(self) -> DefaultDict[str, List[str]]:
        """Process part of speech tags."""
        doc: Doc = self.nlp(self.text)

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


nlp = NLP("Ich bin eine frau")

print(nlp.text)
print(nlp.language)
print(nlp.nlp)
print(nlp.process())
