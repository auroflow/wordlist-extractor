# Make a word list from epub!

This file parses an epub file and generates a list of words in the ebook.

## Usage

The program can run in Python 3.8+. No external library is required!

```
$ python -m epub_wordlist [-h] [-e EPUB] [-k KNOWN_WORDS] [-o OUTPUT]

optional arguments:
  -h, --help            show the help message and exit
  -e EPUB, --epub EPUB  The epub file to process. Default to book.epub.
  -k KNOWN_WORDS, --known-words KNOWN_WORDS
                        The file containing known words. These words are excluded from the word list. Default to known-words.txt.
  -o OUTPUT, --output OUTPUT
                        The output file. Default to wordlist.txt.
```

Apart from the files mentioned above, `data/lemma.en.txt` contains word forms that will be treated as one word. You can modify it as you wish.
