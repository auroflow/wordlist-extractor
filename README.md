# Make a word list from epub!

This file parses an epub file and generates a list of words in the ebook.

## Usage

The program is tested for Python 3.10. No external library is required!

```
$ python -m epub_wordlist --help
usage: __main__.py [-h] [-e EPUB] [-k KNOWN_WORDS] [-o OUTPUT]

Create a word list from an epub file.

optional arguments:
  -h, --help            show this help message and exit
  -e EPUB, --epub EPUB  The epub file to process. Default to book.epub.
  -k KNOWN_WORDS, --known-words KNOWN_WORDS
                        The file containing known words. These words are excluded from the word list. Default to known-words.txt.
  -o OUTPUT, --output OUTPUT
                        The output file. Default to wordlist.txt.
```

Apart from the files mentioned above, `data/lemma.en.txt` contains word forms that will be treated as one word, and `data/words.txt` contains all the words that will be recognized. You can modify them as you wish.

