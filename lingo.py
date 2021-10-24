from abc import ABC, abstractmethod
from spacy import load, explain
from spacy.language import Language
from dataclasses import dataclass, field
from typing import List, Dict
from collections import defaultdict


class NLPModel(ABC):
    @abstractmethod
    def load_model() -> Language:
        pass

class ENModel(NLPModel):
    def load_model() -> Language:
        return load("en_core_web_sm")

class DEModel(NLPModel):
    def load_model() -> Language:
        return load("de_core_news_sm")

@dataclass
class NLP:
    text: str
    model: NLPModel
    nlp: Language = field(init=False, repr=False)
    part_of_speech: Dict[str, List[str]] = field(init=False, default_factory=lambda: defaultdict(list))
    
    def __post_init__(self):
        self.nlp = self.model.load_model()
        
    
    def process(self):
        doc = self.nlp(self.text)
        for token in doc:
            self.part_of_speech["words"].append(token.text)
            self.part_of_speech["lemma"].append(token.lemma_)
            self.part_of_speech["pos"].append(token.pos_)
            self.part_of_speech["detail"].append(explain(token.tag_))
            
            print(token.text, token.lemma_, token.pos_, explain(token.tag_))

class Translator:
    pass

class Lesson:
    pass

class Class:
    pass

def main():
    test = NLP("Doing some tests", ENModel)
    
    test.process()
    
    print(test)

if __name__ == "__main__":
    main()