import os
import re

_words: set[str] = set()
_saved_filename = ''

def get_known_lemmas(pathname: str):
    """
    Get a set of known lemmas from the files containing known lemmas.

    Each line is a lemma.

    Args:
        pathname: The directory containing known word files.

    Returns:
        A set of known lemmas.
    """
    known_lemmas: set[str] = set()

    if not os.path.exists(pathname):
        return known_lemmas

    for filename in os.listdir(pathname):
        fullname = os.path.join(pathname, filename)
        if not os.path.isfile(fullname):
            continue
        with open(fullname, 'r') as f:
            for line in f:
                line = line.split(';')[0].strip()
                if line:
                    known_lemmas.add(line.strip().lower())
    return known_lemmas


_cached_mapping = None


def get_mapping(lemma_filename: str):
    """
    Get a dict object storing mappings from words to their lemmas.

    This function parses the lemma file and creates a dict object storing mappings from
    words to their lemmas.

    The format for each line of the lemma file:

        lemma\t word1 word2 ...

    Example:

        a an

    A line starting with ';' is a comment.

    Args:
        lemma_filename: The file containing the lemma mappings.

    Returns:
        A dict object storing mappings from words to their lemmas.
    """
    global _cached_mapping
    if _cached_mapping is not None:
        return _cached_mapping

    mapping = dict()
    lemmas = set()

    with open(lemma_filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            words = line.split()
            lemmas.add(words[0])
            for word in words:
                if word in lemmas:
                    mapping[word] = word
                else:
                    mapping[word] = words[0]
    _cached_mapping = mapping
    return mapping


def get_words(filename: str):
    """
    Return a set containing all English words in lower case.
    """
    global _saved_filename
    global _words
    
    if _saved_filename == filename and _words:
        return _words

    _saved_filename = filename
    with open(filename) as f:
        for line in f:
            _words.add(line.strip().lower())
    return _words
