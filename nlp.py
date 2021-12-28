"""NLP module containing pos tagging, translation and text to speech functions."""
from dataclasses import dataclass
from typing import List, DefaultDict, Sequence
from collections import defaultdict

import spacy.language
from language import Language, match_language
from translation import detect_language


@dataclass
class NLP:
    """NLP processor and renderer."""
    text: str

    def __post_init__(self) -> None:
        self.language: Language = match_language(detect_language(self.text))
        self.nlp: spacy.language.Language = self.language.load_model()

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
