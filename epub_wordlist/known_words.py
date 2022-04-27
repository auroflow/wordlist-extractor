"""\
This file reads every word from the file containing known words and records its
lemma if it is in the lemma file.

Any words that appear after ';' in a line will be ignored.
"""
from os.path import exists
import re


def get_known_lemmas(filename: str, mapping: dict):
    """
    Get a set of known lemmas from the file containing known words.

    Args:
        filename: The file containing the known words.
        mapping: A dictionary mapping words to their respective lemmas.

    Returns:
        A set of known lemmas.
    """
    known_lemmas: set[str] = set()
    if not exists(filename):
        return known_lemmas
    with open(filename, 'r') as f:
        for line in f:
            line = line.split(';')[0].strip()
            words: list[str] = re.findall(r'\w+', line)
            for word in words:
                word = word.lower()
                if word in mapping:
                    known_lemmas.add(mapping[word])
    return known_lemmas
