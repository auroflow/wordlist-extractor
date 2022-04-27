import argparse
from random import shuffle
from .epub_parser import get_words
from .known_words import get_known_lemmas
from .lemma_creator import get_mapping

# -------------
# Get filenames
# -------------
lemma_filename = 'epub_wordlist/data/lemma.en.txt'
known_words_filename = 'known-words'
book_filename = 'book.epub'
output_filename = 'wordlist.txt'
shuffled = False

argparser = argparse.ArgumentParser(
    description='Create a word list from an epub file.')
argparser.add_argument(
    '-e',  '--epub', help='The epub file to process. Default to {}.'.format(book_filename))
argparser.add_argument(
    '-k', '--known-words', help='The folder which contain known word files. Words in these files are excluded from the word list. Default to {}.'.format(known_words_filename))
argparser.add_argument(
    '-o', '--output', help='The output file. Default to {}.'.format(output_filename))
argparser.add_argument('-s', '--shuffle', action="store_true",
                       help='Shuffle the word list.')
args = argparser.parse_args()
if args.epub:
    book_filename = args.epub
if args.known_words:
    known_words_filename = args.known_words
if args.output:
    output_filename = args.output
if args.shuffle:
    shuffled = True

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
wordlist = list(wordlist)
if shuffled:
    shuffle(wordlist)
else:
    wordlist.sort()
with open(output_filename, 'w') as f:
    for word in wordlist:
        f.write(word + '\n')
