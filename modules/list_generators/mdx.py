import random
import re
from modules.lemmatizers.nltk import NltkLemmatizer
from modules.sentence_tokenizers.nltk import NltkSentTokenizer

from modules.utils.utils import get_known_lemmas, get_mapping
from config import lemma_filename, known_words_path

class ExampleSentenceDictGenerator:
    def generate(self, sentences: list[str], filename: str):
        wordlist: dict[str, list[tuple[str, str]]] = dict()

        mapping = get_mapping(lemma_filename)
        known_lemmas = get_known_lemmas(known_words_path)

        lemmatizer = NltkLemmatizer()

        for sentence in sentences:
            lemma_words = lemmatizer.lemmatize(sentence)
            for lemma, word in lemma_words:
                if lemma not in known_lemmas:
                    if lemma not in wordlist:
                        wordlist[lemma] = []
                    wordlist[lemma].append((word, sentence))

        lemmas = list(wordlist.keys())
        random.shuffle(lemmas)

        with open(filename, 'w') as f:
            for lemma in lemmas:
                f.write(lemma + '\n')
                wordlist[lemma] = set(wordlist[lemma])
                for word, sentence in wordlist[lemma]:
                    sentence = sentence.replace(word, "<strong>" + word + "</strong>")
                    f.write('<p>' + sentence + '</p>\n')
                f.write('</>\n')

if __name__ == '__main__':
    with open('test-text.txt') as f:
        text = f.read()

    t = NltkSentTokenizer()
    sentences = t.get_sentences(text)

    g = ExampleSentenceDictGenerator()
    g.generate(sentences, 'test-list-with-sent.txt')
