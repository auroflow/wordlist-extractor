import argparse
from random import shuffle

from wordlist_extractor.txt_parser import get_words_from_txt
from wordlist_extractor.epub_parser import get_words_from_epub
from wordlist_extractor.known_words import get_known_lemmas
from wordlist_extractor.lemma_creator import get_mapping

# -------------
# Get filenames
# -------------
lemma_filename = 'wordlist_extractor/data/lemma.en.txt'
known_words_filename = 'known-words'
input_filename = 'book.epub'
output_filename = 'wordlist.txt'
shuffled = False

argparser = argparse.ArgumentParser(
    description='Create a word list from an epub file.')
argparser.add_argument(
    '-f',  '--filename', help='The path to the EPUB or TXT file. Default to {}.'.format(input_filename))
argparser.add_argument(
    '-k', '--known-words', help='The folder which contain known word files. Words in these files are excluded from the word list. Default to {}.'.format(known_words_filename))
argparser.add_argument(
    '-o', '--output', help='The output file. Default to {}.'.format(output_filename))
argparser.add_argument('-s', '--shuffle', action="store_true",
                       help='Shuffle the word list.')
args = argparser.parse_args()
if args.filename:
    input_filename = args.filename
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

if input_filename.endswith('.epub'):
    used_words = get_words_from_epub(input_filename)
elif input_filename.endswith('.txt'):
    used_words = get_words_from_txt(input_filename)
else:
    raise ValueError('Unknown file type.')

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
