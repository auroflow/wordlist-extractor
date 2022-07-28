from config import words_filename
from modules.utils.utils import get_words
import spacy
import lemminflect
from word_forms.word_forms import get_word_forms


def get_common_prefix_length(a: str, b: str):
    count = 0
    for m, n in zip(a, b):
        if m == n:
            count += 1
        else:
            break
    return count


class WordFormsLemmatizer:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def lemmatize(self, sentence: str):

        sentence = sentence.replace('’', "'")

        doc = self.nlp(sentence)

        lemma_words: list[tuple[str, str]] = list()
        wordset = get_words(words_filename)

        for original_word in doc:
            lemma = original_word._.lemma().lower()
            if (original_word.pos_ == 'ADV'):
                adjs = get_word_forms(original_word.text)['a']
                if adjs:
                    lemma = adjs.pop().lower()
            if lemma.lower() in wordset:
                lemma_words.append((lemma, original_word.text))

        return lemma_words


if __name__ == '__main__':
    l = WordFormsLemmatizer()
    s = l.lemmatize(
        "'I'm not adorable,' he said adorably. 'You are,' she replied earnestly. 'These are only examples,' I said woefully. 'How boring,' you yawned blearily.")
    print(s)
