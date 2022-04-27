import argparse
from .epub_parser import get_words
from .known_words import get_known_lemmas
from .lemma_creator import get_mapping

# -------------
# Get filenames
# -------------
words_filename = 'data/words.txt'
lemma_filename = 'data/lemma.en.txt'
known_words_filename = 'known-words.txt'
book_filename = 'book.epub'
output_filename = 'wordlist.txt'

argparser = argparse.ArgumentParser(
    description='Create a word list from an epub file.')
argparser.add_argument('--file', '-f', help='The epub file to process.')
argparser.add_argument('--lemma', '-l', help='The lemma file to use.')
argparser.add_argument(
    '--known', '-k', help='The file containing known words. These words are excluded from the word list.')
argparser.add_argument(
    '--words', '-w', help='The file containing all English words to recognize.')
argparser.add_argument('--output', '-o', help='The output file.')
args = argparser.parse_args()
if args.file:
    book_filename = args.file
if args.lemma:
    lemma_filename = args.lemma
if args.known:
    known_words_filename = args.known
if args.words:
    words_filename = args.words
if args.output:
    output_filename = args.output

# ------------------
# Generate word list
# ------------------
mapping = get_mapping(lemma_filename)
known_lemmas = get_known_lemmas(known_words_filename, mapping)
used_words = get_words(book_filename)
wordlist = set()
for word in used_words:
    if word in mapping and mapping[word] not in known_lemmas:
        wordlist.add(mapping[word])
with open(output_filename, 'w') as f:
    for word in sorted(wordlist):
        f.write(word + '\n')
