import random
import re
from modules.lemmatizers.nltk import NltkLemmatizer
from modules.sentence_tokenizers.nltk import NltkSentTokenizer

from modules.utils.utils import get_known_lemmas
from config import known_words_path

class PlainListGenerator:
    def __init__(self, shuffle=False):
        self.shuffle = shuffle

    def generate(self, sentences: list[str], filename: str):
        wordlist: set[str] = set()

        known_lemmas = get_known_lemmas(known_words_path)

        lemmatizer = NltkLemmatizer()

        for sentence in sentences:
            lemma_words = lemmatizer.lemmatize(sentence)
            for lemma, word in lemma_words:
                if lemma not in known_lemmas:
                    wordlist.add(lemma)

        wordlist: list[str] = list(wordlist)
        if self.shuffle:
            random.shuffle(wordlist)
        else:
            wordlist = sorted(wordlist)
        
        with open(filename, 'w') as f:
            for word in wordlist:
                f.write(word + '\n')

    
if __name__ == '__main__':
    with open('test-text.txt') as f:
        text = f.read()

    t = NltkSentTokenizer(text)
    sentences = t.get_sentences()

    g = PlainListGenerator(sentences)
    g.generate('test-list.txt')
