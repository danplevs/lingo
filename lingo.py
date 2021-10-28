"""Main module from the language learning helper.
Contains NLP and translation functionalities, and the data container objects."""
from abc import ABC, abstractmethod
from typing import List, DefaultDict, Sequence
from collections import defaultdict
import spacy
from spacy import displacy


class Language(ABC):
    """Basic representation of a language NLP model."""

    iso_639_1: str

    @classmethod
    @abstractmethod
    def load_model(cls) -> spacy.language.Language:
        """Load model pipeline"""


class English(Language):
    """English NLP model."""

    iso_639_1 = "en"

    @classmethod
    def load_model(cls) -> spacy.language.Language:
        return spacy.load("en_core_web_sm")


class German(Language):
    """German NLP model."""

    iso_639_1 = "de"

    @classmethod
    def load_model(cls) -> spacy.language.Language:
        return spacy.load("de_core_news_sm")


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


class Lesson:
    pass


class Class:
    pass


def main():
    """Main function. It's being used only for testing purposes for now."""
    test = NLP(German)
    print(test.process(("Testing",)))


if __name__ == "__main__":
    main()
