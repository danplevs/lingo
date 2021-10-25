from abc import ABC, abstractmethod
from spacy import load, explain
from spacy.language import Language
from dataclasses import dataclass, field
from typing import List, DefaultDict
from collections import defaultdict
from pandas import DataFrame


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
    part_of_speech: DefaultDict[str, List[str]] = field(init=False)
    
    def __post_init__(self):
        self.nlp = self.model.load_model()
        self.part_of_speech = defaultdict(list)
        
    def process(self):
        doc = self.nlp(self.text)
        for token in doc:
            self.part_of_speech["word"].append(token.text)
            self.part_of_speech["lemma"].append(token.lemma_)
            self.part_of_speech["pos"].append(token.pos_)
            self.part_of_speech["detail"].append(explain(token.tag_))
            
    def table_view(self):
        return DataFrame(self.part_of_speech).query("pos != 'PUNCT'")

class Translator:
    pass

class Lesson:
    pass

class Class:
    pass

def main():
    test = NLP("Doing some tests.", ENModel)
    
    test.process()
    
    print(test.table_view())

if __name__ == "__main__":
    main()