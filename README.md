# Create a word list from EPUB files!

This program parses an EPUB file and generates a list of words used in the ebook.

## Requirements

Python 3.8+. No external library is required!

## Usage

```
$ python -m epub_wordlist [-h] [-e EPUB] [-k KNOWN_WORDS] [-o OUTPUT] [-s]

options:
  -h, --help            show this help message and exit
  -e EPUB, --epub EPUB  The epub file to process. Default to book.epub.
  -k KNOWN_WORDS, --known-words KNOWN_WORDS
                        The folder which contain known word files. Words in these files are excluded from the word list. Default to known-words.
  -o OUTPUT, --output OUTPUT
                        The output file. Default to wordlist.txt.
  -s, --shuffle         Shuffle the word list.
```

The existing files in the `known-words` directory are tailored to my need. You can modify, add or delete them as you wish.

Apart from the files mentioned above, `epub_wordlist/data/lemma.en.txt` contains word forms that will be treated as one word. 

## Licenses

The Python scripts in the `epub_wordlist` directory are released under the 2-Clause BSD License.

The file `epub_wordlist/data/lemma.en.txt` is released under the licenses mentioned in LICENSE.

The example EPUB file `book.epub` contains *Alice's Adventures in Wonderland*, which is in the public domain.
