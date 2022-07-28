import re
from config import words_filename, lemma_filename
from modules.utils.utils import get_words, get_mapping


def get_common_prefix_length(a: str, b: str):
    count = 0
    for m, n in zip(a, b):
        if m == n:
            count += 1
        else:
            break
    return count


class WordListLemmatizer:
    def __init__(self):
        self.mapping = get_mapping(lemma_filename)
        self.words = get_words(words_filename)

    def lemmatize(self, sentence: str):

        lemma_words: list[tuple[str, str]] = list()
        for word in re.findall(r'[\w-]+', sentence):
            lemma = self.mapping.get(word.lower())
            if lemma and lemma in self.words:
                lemma_words.append((lemma, word))

        return lemma_words

if __name__ == '__main__':
    l = WordListLemmatizer()
    s = l.lemmatize(
        "'I'm not adorable,' he said adorably. 'You are,' she replied earnestly. 'These are only examples,' I said half-heartedly. 'How boring,' you yawned blearily.")
    print(s)
