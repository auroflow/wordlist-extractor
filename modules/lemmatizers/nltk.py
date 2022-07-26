from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from config import words_filename
from modules.utils.utils import get_words

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
            lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos))

        lemma_words: list[tuple[str, str]] = list()
        wordset = get_words(words_filename)

        for maybe_word, original_word in zip(lemmas_sent, tokens):
            maybe_word = maybe_word.lower()
            if maybe_word in wordset:
                lemma_words.append((maybe_word, original_word))
        
        return lemma_words


if __name__ == '__main__':
    l = NltkLemmatizer()
    s = l.lemmatize("‘Eighteen pence then,’ she said, and I put the money on the table and limped out, glad to breathe the fresh air of Dundrum.")
    print(s)
