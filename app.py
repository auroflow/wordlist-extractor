import argparse
from modules.list_generators.mdx import ExampleSentenceDictGenerator
from modules.list_generators.wordlist import PlainListGenerator
from modules.sentence_tokenizers.nltk import NltkSentTokenizer
from modules.text_extractors import TextExtractor
from modules.text_extractors.epub import EpubTextExtractor
from modules.text_extractors.txt import TxtTextExtractor
from config import default_input_filename, default_output_filename
# -------------
# Get filenames
# -------------
input_filename = default_input_filename
output_filename = default_output_filename
shuffled = False

argparser = argparse.ArgumentParser(
    description='Create a word list from an epub file.')
argparser.add_argument(
    '-f',  '--filename', help='The path to the EPUB or TXT file. Default to {}.'.format(input_filename))
argparser.add_argument(
    '-o', '--output', help='The output file. Default to {}.'.format(output_filename))
argparser.add_argument('-s', '--shuffle', action="store_true",
                       help='Shuffle the word list.')
args = argparser.parse_args()
if args.filename:
    input_filename = args.filename
if args.output:
    output_filename = args.output
if args.shuffle:
    shuffled = True

# ------------------
# Generate word list
# ------------------

text_extractor: TextExtractor
if input_filename.endswith('.epub'):
    text_extractor = EpubTextExtractor()
elif input_filename.endswith('.txt'):
    text_extractor = TxtTextExtractor()
else:
    raise ValueError('Unknown file type.')

text = text_extractor.get_text(input_filename)

sentence_tokenizer = NltkSentTokenizer()
sentences = sentence_tokenizer.get_sentences(text)

list_generator = PlainListGenerator(shuffle=shuffled)
list_generator.generate(sentences, output_filename)

# mdx_generator = ExampleSentenceDictGenerator()
# mdx_generator.generate(sentences, "dict.txt")
