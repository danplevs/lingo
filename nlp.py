"""NLP module containing pos tagging, translation and text to speech functions."""
from typing import List, DefaultDict, Sequence
from collections import defaultdict

import spacy
from spacy import displacy
from language import Language


class NLP:
    """NLP processor and renderer."""

    def __init__(self, language: Language) -> None:
        self.nlp: spacy.language.Language = language.load_model()

    def process(self, text: Sequence[str]) -> DefaultDict[str, List[str]]:
        """Process part of speech tags."""
        docs: List[spacy.tokens.Doc] = (
            [self.nlp(text)]
            if isinstance(text, str)
            else [self.nlp(phrase) for phrase in text]
        )

        part_of_speech: DefaultDict[str, List[str]] = defaultdict(list)
        for doc in docs:
            for token in doc:
                if not token.is_punct:
                    part_of_speech["word"].append(token.text)
                    part_of_speech["lemma"].append(token.lemma_)
                    part_of_speech["detail"].append(spacy.explain(token.tag_))

        return part_of_speech

    def plot_phrase(self, phrase) -> str:
        """Render a dependency parse tree of a phrase."""
        return displacy.serve(self.nlp(phrase), style="dep")
