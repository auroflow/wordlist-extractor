# Create a word list from EPUB and TXT files!

This program generates a word list out of an EPUB or TXT file, which you can copy to
a vocabulary app and memorize. It can help you keep track of the words you've encountered,
and familiar words will be excluded in future word lists. There is also a script to help
you split a word list in two based on whether you know the word.

## Requirements

Python 3.10. Install the dependencies via `pip`:

```bash
$ python -m venv env

> env\Scripts\activate # Windows
$ source env/bin/activate   # Linux / macOS

(env) $ pip install -r requirements.txt
```

## Usage

### The main word list extractor

```
(env) $ python app.py [-h] [-f FILENAME] [-k KNOWN_WORDS] [-o OUTPUT] [-s]

options:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        The path to the EPUB or TXT file. Default to book.epub.
  -o OUTPUT, --output OUTPUT
                        The output file. Default to wordlist.txt.
  -s, --shuffle         Shuffle the word list.
```

The existing files in the `known-words` directory are tailored to my need. You can modify, add to or delete them as you wish.

Apart from the files mentioned above, `data/lemma.en.txt` contains word forms that will be treated as one word. 

### The wordlist divider script

```
(env) $ python wordlist_divider.py [-h] [-f FILENAME]

options:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        The path to the word list. Default to wordlist.txt.
```

The output names will be `FILENAME.known.txt` for the list of known words and `FILENAME.unknown.txt` for the list of unknown words.

It is recommended that you move `FILENAME.known.txt` to the `known-words` directory so that they will be excluded in future lists.

## Licenses

The Python scripts are released under the 2-Clause BSD License.

The file `data/lemma.en.txt` is released under the licenses mentioned in LICENSE.

The example EPUB file `book.epub` contains *Alice's Adventures in Wonderland*, which is in the public domain.
