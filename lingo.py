"""Main module from the language learning helper.
Contains NLP and translation functionalities, and the data container objects."""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, DefaultDict, Sequence
from collections import defaultdict
import spacy
from spacy.language import Language
from spacy import displacy


class LanguageModel(ABC):
    """Basic representation of a specific NLP model."""
    @abstractmethod
    def load_model(self) -> Language:
        """Load model pipeline"""

class ENModel(LanguageModel):
    """English NLP model."""
    @classmethod
    def load_model(cls) -> Language:
        return spacy.load("en_core_web_sm")

class DEModel(LanguageModel):
    """German NLP model."""
    @classmethod
    def load_model(cls) -> Language:
        return spacy.load("de_core_news_sm")

@dataclass
class NLP:
    """NLP processor and renderer."""
    text: str
    model: LanguageModel
    nlp: Language = field(init=False, repr=False)
    doc: Sequence[spacy.tokens.Doc] = field(init=False, repr=False)

    def __post_init__(self):
        self.nlp = self.model.load_model()
        self.doc = self.nlp(self.text)

    def process(self) -> DefaultDict[str, List[str]]:
        """Process part of speech tags."""
        part_of_speech: DefaultDict[str, List[str]] = defaultdict(list)
        for token in self.doc:
            part_of_speech["word"].append(token.text)
            part_of_speech["lemma"].append(token.lemma_)
            part_of_speech["detail"].append(spacy.explain(token.tag_))

        return part_of_speech

    def plot_dependencies(self) -> str:
        """Render a dependency parse tree."""
        return displacy.render(self.doc, style='dep')


class Translator:
    pass

class Lesson:
    pass

class Class:
    pass

def main():
    """Main function. It's being used only for testing purposes for now."""
    test = NLP("Doing some tests.", ENModel)

    print(test.plot_dependencies())

if __name__ == "__main__":
    main()
