# Create a word list from epub!

This file parses an epub file and generates a list of words in the ebook.

## Requirements

Python 3.8+. No external library is required!

## Usage

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

Apart from the files mentioned above, `data/lemma.en.txt` contains word forms that will be treated as one word. 

## Licenses

The files in the `epub_wordlist` directory is release under the 2-Clause BSD License.

The file `data/lemma.en.txt` is released under the licenses mentioned in LICENSE.
