from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from config import words_filename
from modules.utils.utils import get_words


def get_common_prefix_length(a: str, b: str):
    count = 0
    for m, n in zip(a, b):
        if m == n:
            count += 1
        else:
            break
    return count


class NltkLemmatizer:
    def lemmatize(self, sentence: str):

        sentence = sentence.replace('’', "'")

        def get_wordnet_pos(tag):
            if tag.startswith('J'):
                return wordnet.ADJ
            elif tag.startswith('V'):
                return wordnet.VERB
            elif tag.startswith('N'):
                return wordnet.NOUN
            elif tag.startswith('R'):
                return wordnet.ADV
            else:
                return None

        tokens = word_tokenize(sentence)
        tagged_sent = pos_tag(tokens)

        wnl = WordNetLemmatizer()
        lemmas_sent: list[str] = []
        for tag in tagged_sent:
            wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
            if wordnet_pos == wordnet.ADV:
                lemma = None
                try:
                    possible_lemmas = wordnet.synset(tag[0]+'.r.1').lemmas()
                    for possible_lemma in possible_lemmas:
                        possible_lemma = possible_lemma.pertainyms()[0].name()
                        if len(tag[0]) > get_common_prefix_length(possible_lemma, tag[0]) > max(2, len(tag[0]) - 3):
                            lemma = possible_lemma
                            break
                    if not lemma:
                        lemma = wnl.lemmatize(tag[0], pos=wordnet_pos)
                except:
                    lemma = wnl.lemmatize(tag[0], pos=wordnet_pos)
            else:
                lemma = wnl.lemmatize(tag[0], pos=wordnet_pos)
            lemmas_sent.append(lemma)

        lemma_words: list[tuple[str, str]] = list()
        wordset = get_words(words_filename)

        for maybe_word, original_word in zip(lemmas_sent, tokens):
            maybe_word = maybe_word.lower()
            if maybe_word in wordset:
                lemma_words.append((maybe_word, original_word))

        return lemma_words


if __name__ == '__main__':
    l = NltkLemmatizer()
    s = l.lemmatize(
        "'I'm not adorable,' he said adorably. 'You are,' she replied earnestly. 'These are only examples,' I said woefully. 'How boring,' you yawned blearily.")
    print(s)
